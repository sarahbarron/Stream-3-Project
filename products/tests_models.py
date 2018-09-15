from django.test import TestCase
from .models import Product


class TestProductModel(TestCase):
    ''' test the Product Model '''

    def test_product_model(self):
        ''' test the product model is working '''

        # create a product
        product = Product(name='product',
                          available_stock="10",
                          content='content',
                          price="30",
                          image="img.jpg",
                          num_of_ratings="10",
                          average_rating="5")
        # save product
        product.save()
        # check to see that the product fields equal the saved products values
        self.assertEqual(product.name, "product")
        self.assertEqual(product.content, "content")
        self.assertEqual(product.available_stock, "10")
        self.assertEqual(product.price, "30")
        self.assertEqual(product.image, "img.jpg")
        self.assertEqual(product.num_of_ratings, "10")
        self.assertEqual(product.average_rating, "5")
