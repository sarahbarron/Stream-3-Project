from django.test import TestCase
from .models import Review
from products.models import Product
from django.contrib.auth.models import User


class TestReviewModel(TestCase):
    ''' test the review model '''

    def test_review_model(self):
        ''' test the review model is working '''
        # create an product
        item = Product(name="Product",
                       available_stock="100",
                       content="product content",
                       price="30",
                       image="img.jpg",
                       num_of_ratings="5",
                       average_rating="5")
        # save the product
        item.save()
        # create a user
        user = User.objects.create_user(username='username',
                                        email='myemail@test.com',
                                        password='password')
        # save the user
        user.save()
        # create a review
        review = Review(product=item,
                        user=user, title="title",
                        comment="comment",
                        rating="5",
                        would_you_recommend_to_a_friend="YES")
        # save the review
        review.save()
        # check the the review app fields are the same
        # as the fields of the created review
        self.assertEqual(review.title, "title")
        self.assertEqual(review.comment, "comment")
        self.assertEqual(review.rating, "5")
        self.assertEqual(review.would_you_recommend_to_a_friend, "YES")

    def test_return_review_title_and_rating_as_a_string(self):
        ''' test the return string from the review model '''
        # create a review
        review = Review(title="title", rating="5")
        # save the review
        review.save()
        # check the return string is equal to title-5
        self.assertEqual("title-5", str(review))
