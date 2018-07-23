from django.test import TestCase
from .models import Review
from products.models import Product
from django.contrib.auth.models import User


class TestReviewModel(TestCase):

    def test_review_model(self):
        
        item = Product(name="Product", available_stock="100", content="product content", price="30", image="img.jpg", num_of_ratings="5", average_rating="5")
        item.save()
        
        user = User.objects.create_user(username='username', email='myemail@test.com', password='password')
        user.save()
        
        review = Review(product=item, user=user, title="title", comment="comment", rating="5", would_you_recommend_to_a_friend="YES")
        review.save()
        self.assertEqual(review.title, "title")
        self.assertEqual(review.comment, "comment")
        self.assertEqual(review.rating, "5")
        self.assertEqual(review.would_you_recommend_to_a_friend, "YES")
    
    def test_return_review_title_and_rating_as_a_string(self):
        review = Review(title="title", rating="5")
        review.save()
        self.assertEqual("title-5", str(review))
        
