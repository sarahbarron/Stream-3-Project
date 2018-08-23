from django.test import TestCase
from .models import Order, OrderLineItem
from django.utils import timezone
from django.contrib.auth.models import User
from products.models import Product

# Test Order Model
class TestOrderModel(TestCase):

    # test order model
    def test_order_model(self):
        # create an order
        order = Order(full_name = 'fullname', phone_number ='12345', street_address1='first', street_address2='last', town_or_city='waterford', country='Ireland', postcode = 'eircode', date ="2018-06-01")
        # save the order
        order.save()
        
        # check that all fields are equal to the order details
        self.assertEqual(order.full_name, "fullname")
        self.assertEqual(order.phone_number, "12345")
        self.assertEqual(order.street_address1, "first")
        self.assertEqual(order.street_address2, "last")
        self.assertEqual(order.town_or_city, "waterford")
        self.assertEqual(order.country, "Ireland")
        self.assertEqual(order.postcode, "eircode")
        self.assertEqual(order.date, "2018-06-01")
    
    # test order line item model
    def test_order_Line_Item_model(self):
        # create an order
        order = Order(full_name = 'fullname', phone_number ='12345', street_address1='first', street_address2='last', town_or_city='waterford', country='Ireland', postcode = 'eircode', date ="2018-06-01")
        # save the order
        order.save()
        
        # create a product
        item = Product(name="Product", available_stock="100", content="product content", price="30", image="img.jpg", num_of_ratings="5", average_rating="5")
        # save the product
        item.save()
        
        # create a user
        user = User.objects.create_user(username='username', email='myemail@test.com', password='password')
        # save the user
        user.save()
        
        # create an order line item with the user, product, order, quantity and status
        order_line_item = OrderLineItem(user=user, product=item, order=order, quantity="1", status="Delivered")
        
        # check the order_line_item fields are equal to the values of order_line_item 
        self.assertEqual(order_line_item.order.full_name, "fullname")
        self.assertEqual(order_line_item.product.name, "Product")
        self.assertEqual(order_line_item.user.username, "username")
        self.assertEqual(order_line_item.quantity, "1")
        self.assertEqual(order_line_item.status, "Delivered")
        self.assertNotEqual(order_line_item.status, "Awaiting Dispatch")
    
    # test return value is the expected string
    def test_return_order_id_date_and_fullname_as_a_string(self):
        # create an order
        order = Order(full_name='fullname', date='2018-06-01')
        order.save()
        # check the return value is what is expected
        self.assertEqual("1-2018-06-01-fullname", str(order))
    
    # test return value is the expected string
    def test_return_order_line_item_quantity_product_name_and_product_price_as_a_string(self):
        # create a product
        product = Product(name="product", price="30")
        # create an order
        order = OrderLineItem(quantity='1', product=product)
        #  check the return value is what is expected
        self.assertEqual("1 product @ 30", str(order))
        