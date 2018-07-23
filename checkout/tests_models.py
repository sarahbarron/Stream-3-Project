from django.test import TestCase
from .models import Order, OrderLineItem
from django.utils import timezone
from django.contrib.auth.models import User
from products.models import Product


class TestOrderModel(TestCase):

    def test_orderr_model(self):
        order = Order(full_name = 'fullname', phone_number ='12345', street_address1='first', street_address2='last', town_or_city='waterford', country='Ireland', postcode = 'eircode', date ="2018-06-01")
        order.save()
        
        self.assertEqual(order.full_name, "fullname")
        self.assertEqual(order.phone_number, "12345")
        self.assertEqual(order.street_address1, "first")
        self.assertEqual(order.street_address2, "last")
        self.assertEqual(order.town_or_city, "waterford")
        self.assertEqual(order.country, "Ireland")
        self.assertEqual(order.postcode, "eircode")
        self.assertEqual(order.date, "2018-06-01")
    
    def test_order_Line_Item_model(self):
        order = Order(full_name = 'fullname', phone_number ='12345', street_address1='first', street_address2='last', town_or_city='waterford', country='Ireland', postcode = 'eircode', date ="2018-06-01")
        order.save()
        
        item = Product(name="Product", available_stock="100", content="product content", price="30", image="img.jpg", num_of_ratings="5", average_rating="5")
        item.save()
        
        user = User.objects.create_user(username='username', email='myemail@test.com', password='password')
        user.save()
        
        order_line_item = OrderLineItem(user=user, product=item, order=order, quantity="1", status="Delivered")
        
        self.assertEqual(order_line_item.quantity, "1")
        self.assertEqual(order_line_item.status, "Delivered")
        self.assertNotEqual(order_line_item.status, "Awaiting Dispatch")
    
    def test_return_order_id_date_and_fullname_as_a_string(self):
        order = Order(id='1', full_name='fullname', date='2018-06-01')
        self.assertEqual("1-2018-06-01-fullname", str(order))
    
    def test_return_order_line_item_quantity_product_name_and_product_price_as_a_string(self):
        product = Product(name="product", price="30")
        order = OrderLineItem(quantity='1', product=product)
        self.assertEqual("1 product @ 30", str(order))
        