from django.test import TestCase
from products.models import Product
from django.shortcuts import get_object_or_404


class TestCartViews(TestCase):
    ''' test the cart views '''

    def test_view_cart_view(self):
        ''' test viewing the cart '''

        # view a cart url
        page = self.client.get("/cart/")
        # check status code is 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is cart.html page
        self.assertTemplateUsed(page, "cart.html")

    def test_add_to_cart_view(self):
        ''' test add to cart '''

        # create a Product
        item = Product(name="Product",
                       available_stock="4",
                       content="product content",
                       price="30",
                       image="img.jpg",
                       num_of_ratings="5",
                       average_rating="5")
        # save the product
        item.save()
        # post product and quantity to cart
        page = self.client.post("/cart/add/{0}".format(item.id),
                                data={'quantity': '20'},
                                follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is products.html
        self.assertTemplateUsed(page, "products.html")

    def test_add_to_cart_when_product_is_already_in_the_cart(self):
        ''' test add to cart when the product
        is already in the cart '''

        # create a Product
        item = Product(name="Product",
                       available_stock="100",
                       content="product content",
                       price="30",
                       image="img.jpg",
                       num_of_ratings="5",
                       average_rating="5")
        # save the product
        item.save()
        # post product and quantity to cart
        page = self.client.post("/cart/add/{0}".format(item.id),
                                data={'quantity': '3'},
                                follow=True)
        # post same product and quantity to cart
        page = self.client.post("/cart/add/{0}".format(item.id),
                                data={'quantity': '1'},
                                follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is products.html
        self.assertTemplateUsed(page, "products.html")

    def test_adjust_cart_view(self):
        ''' test adjusting the quantity in the cart '''

        # create an item
        item = Product(available_stock="4",
                       name="Product",
                       content="product content",
                       price="30",
                       image="img.jpg",
                       num_of_ratings="5",
                       average_rating="5")
        # save the item
        item.save()
        # post the product id and ammended quantity
        page = self.client.post("/cart/adjust/{0}".format(item.id),
                                data={"quantity": 100},
                                follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        #  # check Template Used is cart.html page
        self.assertTemplateUsed(page, "cart.html")

    def test_removing_an_item_from_the_cart(self):
        ''' test removing an item from the cart '''

        # create a Product
        item = Product(name="Product",
                       available_stock="100",
                       content="product content",
                       price="30",
                       image="img.jpg",
                       num_of_ratings="5",
                       average_rating="5")
        # save the product
        item.save()
        # post product and quantity to cart
        page = self.client.post("/cart/add/{0}".format(item.id),
                                data={'quantity': '3'},
                                follow=True)
        # post same product and quantity to cart
        page = self.client.post("/cart/adjust/{0}".format(item.id),
                                data={'quantity': '0'},
                                follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is products.html
        self.assertTemplateUsed(page, "cart.html")
