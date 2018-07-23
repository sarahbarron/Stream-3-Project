from django.test import TestCase
from .models import Product


class TestProductModel(TestCase):

    def test_product_model(self):
        product = Product(name = 'product', available_stock = "10", content ='content', price = "30", image = "img.jpg", num_of_ratings="10", average_rating="5")
        product.save()
        self.assertEqual(product.name, "product")
        self.assertEqual(product.content, "content")
        self.assertEqual(product.available_stock, "10")
        self.assertEqual(product.price, "30")
        self.assertEqual(product.image, "img.jpg")
        self.assertEqual(product.num_of_ratings, "10")
        self.assertEqual(product.average_rating, "5")