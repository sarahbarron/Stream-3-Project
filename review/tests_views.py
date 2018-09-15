from django.test import TestCase
from django.contrib.auth.models import User
from .models import Review
from products.models import Product


class TestViewReviews(TestCase):
    ''' test review views '''

    def test_get_reviews_page(self):
        ''' test get reviews page '''

        # create a product
        item = Product(name="Product",
                       available_stock="100",
                       content="product content",
                       price="30",
                       image="img.jpg",
                       num_of_ratings="5",
                       average_rating="5")
        # save the product
        item.save()
        # reviews url with product id
        page = self.client.get("/reviews/{0}/".format(item.id),
                               follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check the Template used is allreviews.html
        self.assertTemplateUsed(page, "allreviews.html")

    # test view full review
    def test_view_full_review_page(self):
        ''' test view full review view '''

        # create a product
        item = Review(title='test title',
                      comment='test content',
                      rating='5',
                      would_you_recommend_to_a_friend='YES')
        # save a product
        item.save()
        # view full review url with review id
        # check the status code is 200
        page = self.client.get("/reviews/full_review/{0}/".format(item.id))
        self.assertEqual(page.status_code, 200)
        # check the Template Used is fullreview.html
        self.assertTemplateUsed(page, "fullreview.html")


class TestNewReview(TestCase):
    ''' test adding a new review '''

    def test_add_review_page(self):
        ''' test add a review '''

        # create a user
        user = User.objects.create_user(username='username',
                                        email='myemail@test.com',
                                        password='password')
        # login user
        self.client.login(username='username',
                          password='password')
        # create a product
        item = Product(name="Product",
                       available_stock="100",
                       content="product content",
                       price="30",
                       image="img.jpg",
                       num_of_ratings="5",
                       average_rating="5")
        # save the product
        item.save()
        # new review url with product id
        page = self.client.get("/reviews/new/{0}/".format(item.id),
                               follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check template used reviewform.html
        self.assertTemplateUsed(page, "reviewform.html")

    def test_add_review_page_with_no_one_logged_in(self):
        ''' test add review with no-one logged in '''

        # create a product
        item = Product(name="Product",
                       available_stock="100",
                       content="product content",
                       price="30",
                       image="img.jpg",
                       num_of_ratings="5",
                       average_rating="5")
        # save a product
        item.save()
        # add a new review with product id
        page = self.client.get("/reviews/new/{0}/".format(item.id),
                               follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check the template used is login.html
        self.assertTemplateUsed(page, "login.html")

    def test_post_to_add_review(self):
        ''' test POST to add review '''

        # create a user
        user = User.objects.create_user(username='username',
                                        email='myemail@test.com',
                                        password='password')
        # login the user
        self.client.login(username='username',
                          password='password')
        # create a product
        item = Product(name="Product",
                       available_stock="100",
                       content="product content",
                       price="30",
                       image="img.jpg",
                       num_of_ratings="5",
                       average_rating="5")
        # save the product
        item.save()
        # post the review data
        page = self.client.post("/reviews/new/{0}/".format(item.id),
                                {'title': 'title',
                                 'comment': 'comment',
                                 'rating': '5',
                                 'would_you_recommend_to_a_friend': 'YES'},
                                follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check the template used is login.html
        self.assertTemplateUsed(page, "products.html")


class TestEditReview(TestCase):
    ''' test the edit review view '''

    def test_edit_review_page_by_creater_of_review(self):
        ''' Test edit review when person logged in is the review creator '''

        # create a user
        user = User.objects.create_user(username='username',
                                        email='myemail@test.com',
                                        password='password')
        # login user
        self.client.login(username='username',
                          password='password')
        # create a review
        review = Review(user=user,
                        title='test title',
                        comment='test content',
                        rating='5',
                        would_you_recommend_to_a_friend='YES')
        # save the review
        review.save()
        # edit review with review id url
        page = self.client.get("/reviews/edit/{0}/".format(review.id),
                               follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check the template used reviewform.html
        self.assertTemplateUsed(page, "reviewform.html")

    def test_edit_review_page_with_no_one_logged_in(self):
        ''' test the edit review form with no-one logged in '''

        # create the creater of the review
        review_creator = User.objects.create_user(username='review',
                                                  email='review@test.com',
                                                  password='review')
        # create an product
        item = Product(name="Product",
                       available_stock="100",
                       content="product content",
                       price="30",
                       image="img.jpg",
                       num_of_ratings="10",
                       average_rating="5")
        # save the product
        item.save()
        # create  a review
        review = Review(user=review_creator,
                        product=item,
                        title='test title',
                        comment='test content',
                        rating='5',
                        would_you_recommend_to_a_friend='YES')
        # save the review
        review.save()
        # edit review url with review id
        page = self.client.get("/reviews/edit/{0}/".format(review.id),
                               follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check the template used is login.html
        self.assertTemplateUsed(page, "login.html")

    def test_edit_review_when_logged_in_but_not_as_the_review_creator(self):
        ''' test edit review when logged in as someone other than
        the review creator '''

        # create the review creator user
        review_creator = User.objects.create_user(username='review',
                                                  email='review@test.com',
                                                  password='review')
        # crate a review
        review = Review(user=review_creator,
                        title='test title',
                        comment='test content',
                        rating='5',
                        would_you_recommend_to_a_friend='YES')
        # save the review
        review.save()
        # logged in a different user to the review creator
        logged_in_user = User.objects.create_user(username='username',
                                                  email='myemail@test.com',
                                                  password='password')
        self.client.login(username='username',
                          password='password')
        # edit review url
        page = self.client.get("/reviews/edit/{0}/".format(review.id),
                               follow=True)
        # check status code is 200
        self.assertEqual(page.status_code, 200)
        # check the template used is index.html
        self.assertTemplateUsed(page, "index.html")

    def test_post_to_edit_review(self):
        ''' test post to edit review  '''

        # create a user
        user = User.objects.create_user(username='username',
                                        email='myemail@test.com',
                                        password='password')
        # login the user
        self.client.login(username='username',
                          password='password')
        # create a product
        item = Product(name="Product",
                       available_stock="100",
                       content="product content",
                       price="30",
                       image="img.jpg",
                       num_of_ratings="5",
                       average_rating="5")
        # save the product
        item.save()
        # create a review
        review = Review(product=item,
                        user=user,
                        title='title',
                        comment='comment',
                        rating='5',
                        would_you_recommend_to_a_friend="YES")
        # save the review
        review.save()
        # post to the edit url
        page = self.client.post("/reviews/edit/{0}/".format(review.id),
                                {'title': 'change',
                                 'comment': 'change',
                                 'rating': '1',
                                 'would_you_recommend_to_a_friend': 'NO'},
                                follow=True)
        # check status code is 200
        self.assertEqual(page.status_code, 200)
        # check the template used is profile.html
        self.assertTemplateUsed(page, "profile.html")

    def test_post_to_edit_review_when_num_of_rating_is_1(self):
        '''  test post to edit review when the number of ratings is 1 '''

        # create a user
        user = User.objects.create_user(username='username',
                                        email='myemail@test.com',
                                        password='password')
        # login the user
        self.client.login(username='username',
                          password='password')
        # create a product
        item = Product(name="Product",
                       available_stock="100",
                       content="product content",
                       price="30",
                       image="img.jpg",
                       num_of_ratings="1",
                       average_rating="5")
        # save the product
        item.save()
        # create a review
        review = Review(product=item,
                        user=user,
                        title='title',
                        comment='comment',
                        rating='5',
                        would_you_recommend_to_a_friend="YES")
        # save review
        review.save()
        # post to the edit review url
        page = self.client.post("/reviews/edit/{0}/".format(review.id),
                                {'title': 'change',
                                 'comment': 'change',
                                 'rating': '1',
                                 'would_you_recommend_to_a_friend': 'NO'},
                                follow=True)
        # check status code is 200
        self.assertEqual(page.status_code, 200)
        # check the template used is profile.html
        self.assertTemplateUsed(page, "profile.html")


class TestDeleteReview(TestCase):
    ''' test delete view '''

    def test_to_delete_a_review(self):
        ''' test delete review when logged
        in as the user who wrote the review '''

        # create a user
        user = User.objects.create_user(username='username',
                                        email='myemail@test.com',
                                        password='password')
        self.client.login(username='username',
                          password='password')
        # create a product
        item = Product(name="Product",
                       available_stock="100",
                       content="product content",
                       price="30",
                       image="img.jpg",
                       num_of_ratings="10",
                       average_rating="5")
        # save the product
        item.save()
        # create a review
        review = Review(user=user,
                        product=item,
                        title='test title',
                        comment='test content',
                        rating='5',
                        would_you_recommend_to_a_friend='YES')
        # save the review
        review.save()
        # delete review url
        page = self.client.get("/reviews/delete/{0}/".format(review.id),
                               follow=True)
        # check status code is 200
        self.assertEqual(page.status_code, 200)
        # check the template used is profile.html
        self.assertTemplateUsed(page, "profile.html")

    def test_to_delete_a_review_with_no_one_logged_in(self):
        ''' test delete review when no-one is logged in '''

        # create a product
        item = Product(name="Product",
                       available_stock="100",
                       content="product content",
                       price="30",
                       image="img.jpg",
                       num_of_ratings="10",
                       average_rating="5")
        # save the product
        item.save()
        # create a user
        review_creator = User.objects.create_user(username='review',
                                                  email='review@test.com',
                                                  password='review')
        # creaate a review
        review = Review(user=review_creator,
                        product=item,
                        title='test title',
                        comment='test content',
                        rating='5',
                        would_you_recommend_to_a_friend='YES')
        # save the review
        review.save()
        # delete review url
        page = self.client.get("/reviews/delete/{0}/".format(review.id),
                               follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check the template used is login.html
        self.assertTemplateUsed(page, "login.html")

    def test_delete_review_when_logged_in_not_as_the_review_creator(self):
        ''' test login when logged in as someone
        other than the review creator '''

        # create a review creator user
        review_creator = User.objects.create_user(username='review',
                                                  email='review@test.com',
                                                  password='review')
        # create a second user
        user = User.objects.create_user(username='username',
                                        email='myemail@test.com',
                                        password='password')
        # create a Product
        item = Product(name="Product",
                       available_stock="100",
                       content="product content",
                       price="30",
                       image="img.jpg",
                       num_of_ratings="10",
                       average_rating="5")
        # save the product
        item.save()
        # create a review
        review = Review(user=review_creator,
                        product=item,
                        title='test title',
                        comment='test content',
                        rating='5',
                        would_you_recommend_to_a_friend='YES')
        # save the review
        review.save()
        # login the second user
        self.client.login(username='username',
                          password='password')
        # delete review url
        page = self.client.get("/reviews/delete/{0}/".format(review.id),
                               follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check the template used is index.html
        self.assertTemplateUsed(page, "index.html")

    def test_to_delete_a_review_when_number_of_reviews_returns_to_zero(self):
        '''  test delete a review when the number of reviews returns to 0 '''

        # create a user
        user = User.objects.create_user(username='username',
                                        email='myemail@test.com',
                                        password='password')
        # login user
        self.client.login(username='username',
                          password='password')
        # create a product
        item = Product(name="Product",
                       available_stock="100",
                       content="product content",
                       price="30",
                       image="img.jpg",
                       num_of_ratings="1",
                       average_rating="5")
        # save the product
        item.save()
        # create a review
        review = Review(user=user,
                        product=item,
                        title='test title',
                        comment='test content',
                        rating='5',
                        would_you_recommend_to_a_friend='YES')
        # save the review
        review.save()
        # delete review url
        page = self.client.get("/reviews/delete/{0}/".format(review.id),
                               follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check the template used is profile.html
        self.assertTemplateUsed(page, "profile.html")
