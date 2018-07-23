from django.test import TestCase
from django.contrib.auth.models import User
from .models import Review
from products.models import Product

# new_review, edit_review, view_review,full_review, delete_review 

class TestReviewsViews(TestCase):

    def test_get_reviews_page(self):
        item = Product(name="Product", available_stock="100", content="product content", price="30", image="img.jpg", num_of_ratings="5", average_rating="5")
        item.save()
        page = self.client.get("/reviews/{0}/".format(item.id), follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "allreviews.html")
    
    def test_view_full_review_page(self):
        
        item = Review(title='test title', comment='test content', rating = '5', would_you_recommend_to_a_friend = 'YES', )
        item.save()
        
        page = self.client.get("/reviews/full_review/{0}/".format(item.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "fullreview.html")
    
    def test_add_review_page(self):
        user = User.objects.create_user(username = 'username', email = 'myemail@test.com', password='password')
        self.client.login(username = 'username', password = 'password')
    
        item = Product(name="Product", available_stock="100", content="product content", price="30", image="img.jpg", num_of_ratings="5", average_rating="5")
        item.save()
        
        page = self.client.get("/reviews/new/{0}/".format(item.id) , follow = True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "reviewform.html")
    
    def test_edit_review_page(self):
        user = User.objects.create_user(username = 'username', email = 'myemail@test.com', password='password')
        self.client.login(username = 'username', password = 'password')
        
        review = Review(user=user, title='test title', comment='test content', rating = '5', would_you_recommend_to_a_friend = 'YES', )
        review.save()
        
        page = self.client.get("/reviews/edit/{0}/".format(review.id), follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "reviewform.html")
    
    def test_to_delete_a_review(self):
        user = User.objects.create_user(username = 'username', email = 'myemail@test.com', password='password')
        self.client.login(username = 'username', password = 'password')
        
        item = Product(name="Product", available_stock="100", content="product content", price="30", image="img.jpg", num_of_ratings="10", average_rating="5")
        item.save()
        
        review = Review(user=user, product=item, title='test title', comment='test content', rating = '5', would_you_recommend_to_a_friend = 'YES', )
        review.save()
        
        page = self.client.get("/reviews/delete/{0}/".format(review.id), follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")
    
    
    def test_add_review_page_with_no_one_logged_in(self):
        item = Product(name="Product", available_stock="100", content="product content", price="30", image="img.jpg", num_of_ratings="5", average_rating="5")
        item.save()
        
        page = self.client.get("/reviews/new/{0}/".format(item.id) , follow = True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
    
    def test_edit_review_page_with_no_one_logged_in(self):
        review_creator = User.objects.create_user(username = 'review', email = 'review@test.com', password='review')
        
        item = Product(name="Product", available_stock="100", content="product content", price="30", image="img.jpg", num_of_ratings="10", average_rating="5")
        item.save()
        
        review = Review(user=review_creator, product=item, title='test title', comment='test content', rating = '5', would_you_recommend_to_a_friend = 'YES', )
        review.save()
        
        page = self.client.get("/reviews/edit/{0}/".format(review.id), follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
    
    def test_to_delete_a_review_with_no_one_logged_in(self):
        item = Product(name="Product", available_stock="100", content="product content", price="30", image="img.jpg", num_of_ratings="10", average_rating="5")
        item.save()
        
        review_creator = User.objects.create_user(username = 'review', email = 'review@test.com', password='review')
        
        review = Review(user=review_creator, product=item, title='test title', comment='test content', rating = '5', would_you_recommend_to_a_friend = 'YES', )
        review.save()
        
        page = self.client.get("/reviews/delete/{0}/".format(review.id), follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")

    def test_edit_review_page_when_logged_in_but_not_as_the_review_creator(self):
        
        review_creator = User.objects.create_user(username = 'review', email = 'review@test.com', password='review')
        
        logged_in_user = User.objects.create_user(username = 'username', email = 'myemail@test.com', password='password')
        self.client.login(username = 'username', password = 'password')
        
        review = Review(user=review_creator, title='test title', comment='test content', rating = '5', would_you_recommend_to_a_friend = 'YES', )
        review.save()
        
        page = self.client.get("/reviews/edit/{0}/".format(review.id), follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
    
    def test_to_delete_a_review_when_logged_in_but_not_as_the_review_creator(self):
        review_creator = User.objects.create_user(username = 'review', email = 'review@test.com', password='review')
        
        user = User.objects.create_user(username = 'username', email = 'myemail@test.com', password='password')
        self.client.login(username = 'username', password = 'password')
        
        item = Product(name="Product", available_stock="100", content="product content", price="30", image="img.jpg", num_of_ratings="10", average_rating="5")
        item.save()
        
        review = Review(user=review_creator, product=item, title='test title', comment='test content', rating = '5', would_you_recommend_to_a_friend = 'YES', )
        review.save()
        
        
        
        page = self.client.get("/reviews/delete/{0}/".format(review.id), follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
    
    def test_post_to_add_review(self):
        #create a user
        user = User.objects.create_user(username = 'username', email = 'myemail@test.com', password='password')
        #login the user
        self.client.login(username = 'username', password = 'password')
        # create a product
        item = Product(id=1, name="Product", available_stock="100", content="product content", price="30", image="img.jpg", num_of_ratings="5", average_rating="5")
        # save the product
        item.save()
        # post the review data
        self.client.post("/reviews/new/{0}/".format(item.id), {'title':'title','comment':'comment', 'rating':'5', 'would_you_recommend_to_a_friend':'YES'},follow=True)

    def test_post_to_edit_review(self):
        #create a user
        user = User.objects.create_user(username = 'username', email = 'myemail@test.com', password='password')
        #login the user
        self.client.login(username = 'username', password = 'password')
       
        # create a product
        item = Product(id=1, name="Product", available_stock="100", content="product content", price="30", image="img.jpg", num_of_ratings="5", average_rating="5")
        # save the product
        item.save()
        
        # create a review
        review = Review(id=1, product=item, user=user, title='title', comment='comment', rating='5', would_you_recommend_to_a_friend="YES")
        review.save()
        
        self.client.post("/reviews/edit/{0}/".format(review.id), {'title':'change','comment':'change', 'rating':'1', 'would_you_recommend_to_a_friend':'NO'},follow=True)
    
    def test_post_to_edit_review_when_num_of_rating_is_1(self):
        #create a user
        user = User.objects.create_user(username = 'username', email = 'myemail@test.com', password='password')
        #login the user
        self.client.login(username = 'username', password = 'password')
       
        # create a product
        item = Product(id=1, name="Product", available_stock="100", content="product content", price="30", image="img.jpg", num_of_ratings="1", average_rating="5")
        # save the product
        item.save()
        
        # create a review
        review = Review(id=1, product=item, user=user, title='title', comment='comment', rating='5', would_you_recommend_to_a_friend="YES")
        review.save()
        
        self.client.post("/reviews/edit/{0}/".format(review.id), {'title':'change','comment':'change', 'rating':'1', 'would_you_recommend_to_a_friend':'NO'},follow=True)
    
    def test_to_delete_a_review_when_number_of_reviews_is_0(self):
        user = User.objects.create_user(username = 'username', email = 'myemail@test.com', password='password')
        self.client.login(username = 'username', password = 'password')
        
        item = Product(name="Product", available_stock="100", content="product content", price="30", image="img.jpg", num_of_ratings="1", average_rating="5")
        item.save()
        
        review = Review(user=user, product=item, title='test title', comment='test content', rating = '5', would_you_recommend_to_a_friend = 'YES', )
        review.save()
        
        page = self.client.get("/reviews/delete/{0}/".format(review.id), follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")
    
    
        