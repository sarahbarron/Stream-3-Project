from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


class TestPostssViews(TestCase):
    ''' Test Post Views '''

    def test_get_post_page(self):
        ''' test getting all posts page '''

        # posts url
        page = self.client.get("/posts/")
        # check status code 200
        self.assertEqual(page.status_code, 200)
        # check you are directed to the allposts.html page
        self.assertTemplateUsed(page, "allposts.html")

    def test_view_full_post_page(self):
        ''' test full post page view '''

        # create a post
        post = Post(title="Title",
                    content='content',
                    category='test category',
                    tag='test tag',
                    view_on_front_page='True')
        # save a post
        post.save()
        # view full post url with post id
        page = self.client.get("/posts/{0}".format(post.id), follow=True)
        # check status code is 200
        self.assertEqual(page.status_code, 200)
        # check that you are directed to the fullpost.html page
        self.assertTemplateUsed(page, "fullpost.html")


class TestAddPostView(TestCase):
    ''' Test Add Post view '''

    def test_create_a_post_view_to_get_blog_post_form(self):
        ''' test create_or_edit_post view to bring
        you to the blog post form '''

        # create a user with staff status
        user = User.objects.create_user(username='username',
                                        email='myemail@test.com',
                                        password='password',
                                        is_staff=True)
        # login the user
        self.client.login(username='username',
                          password='password')
        # posts new url
        page = self.client.get("/posts/new/", follow=True)
        # check there is a status code of 200
        self.assertEqual(page.status_code, 200)
        # check the template used is blogpostform.html
        self.assertTemplateUsed(page, "blogpostform.html")

    def test_create_a_post_with_no_one_logged_in(self):
        ''' test trying to create a post when no-one is logged in '''

        # posts new url
        page = self.client.get("/posts/new/", follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check the template used is login.html
        self.assertTemplateUsed(page, "login.html")

    def test_create_a_post_if_logged_in_user_has_no_staff_status(self):
        ''' test creating a post if logged in
        user does not have staff status '''

        # create a user with no staff status
        user = User.objects.create_user(username='username',
                                        email='myemail@test.com',
                                        password='password')
        # login the user
        self.client.login(username='username',
                          password='password')
        # posts new url
        page = self.client.get("/posts/new/", follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check template used is index.html
        self.assertTemplateUsed(page, "index.html")

    def test_create_a_post_with_POST_method(self):
        ''' test posting a new post '''

        # create a user with staff status
        user = User.objects.create_user(username='username',
                                        email='myemail@test.com',
                                        password='password',
                                        is_staff=True, )
        # login the user
        self.client.login(username='username',
                          password='password')
        # post the post data
        page = self.client.post("/posts/new/",
                                {'title': 'Title',
                                 'content': 'content',
                                 'category': 'test category',
                                 'tag': 'test tag',
                                 'view_on_front_page': 'True'},
                                follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check template used is fullpost.html
        self.assertTemplateUsed(page, "fullpost.html")


class TestEditPostView(TestCase):
    ''' Test edit post view '''

    # test edit post page
    def test_edit_post_page(self):
        # create a user with staff status
        user = User.objects.create_user(username='username',
                                        email='myemail@test.com',
                                        password='password',
                                        is_staff=True)
        # login the user
        self.client.login(username='username',
                          password='password')
        # create a post
        post = Post(title="Title",
                    content='content',
                    category='test category',
                    tag='test tag',
                    view_on_front_page='True')
        # save the post
        post.save()
        # edit post url with post id
        page = self.client.get("/posts/{0}/edit/".format(post.id),
                               follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check the template used is blogpostform.html
        self.assertTemplateUsed(page, "blogpostform.html")

    def test_edit_post_page_with_no_one_logged_in(self):
        ''' test edit post with no-one logged in '''

        # create a post
        post = Post(title="Title",
                    content='content',
                    category='test category',
                    tag='test tag',
                    view_on_front_page='True')
        # save the post
        post.save()
        # edit post url with post id
        page = self.client.get("/posts/{0}/edit/".format(post.id), follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check template used is login.html
        self.assertTemplateUsed(page, "login.html")

    def test_edit_post_page_if_logged_in_person_has_no_staff_status(self):
        ''' test edit post if person logged in is not a staff member '''

        # create a user with no staff status
        user = User.objects.create_user(username='username',
                                        email='myemail@test.com',
                                        password='password')
        # login the user
        self.client.login(username='username',
                          password='password')
        # create a post
        post = Post(title="Title",
                    content='content',
                    category='test category',
                    tag='test tag',
                    view_on_front_page='True')
        # save the post
        post.save()
        # edit post url with post id
        page = self.client.get("/posts/{0}/edit/".format(post.id), follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check th template used is index.html
        self.assertTemplateUsed(page, "index.html")

    def test_edit_post_with_POST_method(self):
        ''' test posting an edited post '''

        # create a user with staff status
        user = User.objects.create_user(username='username',
                                        email='myemail@test.com',
                                        password='password',
                                        is_staff=True, )
        # login the user
        self.client.login(username='username',
                          password='password')
        # create a post
        post = Post(title="Title",
                    content='content',
                    category='test category',
                    tag='test tag',
                    view_on_front_page='True')
        # save the post
        post.save()
        # post the post data using the edit post url
        page = self.client.post("/posts/{0}/edit/".format(post.id),
                                {'title': 'change',
                                 'content': 'change',
                                 'category': 'change',
                                 'tag': 'change',
                                 'view_on_front_page': 'False'},
                                follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check template used is fullpost.html
        self.assertTemplateUsed(page, "fullpost.html")


class TestDeletPostView(TestCase):
    ''' test delete posts '''

    def test_to_delete_a_post(self):
        ''' test deleting a post '''

        # create a user with staff status
        user = User.objects.create_user(username='username',
                                        email='myemail@test.com',
                                        password='password',
                                        is_staff=True)
        # login the user
        self.client.login(username='username',
                          password='password')
        # create a post
        post = Post(title="Title",
                    content='content',
                    category='test category',
                    tag='test tag',
                    view_on_front_page='True')
        # save the post
        post.save()
        # delete post url with post id
        page = self.client.get("/posts/{0}/delete/".format(post.id),
                               follow=True)
        # check the error status is 200
        self.assertEqual(page.status_code, 200)
        # check the template used is allposts.html
        self.assertTemplateUsed(page, "allposts.html")

    def test_to_delete_a_post_with_no_one_logged_in(self):
        ''' test to delete post when no-one is logged in '''

        # create a post
        post = Post(title="Title",
                    content='content',
                    category='test category',
                    tag='test tag',
                    view_on_front_page='True')
        # save a post
        post.save()
        # delete post url with post id
        page = self.client.get("/posts/{0}/delete/".format(post.id),
                               follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check the template used is login.html
        self.assertTemplateUsed(page, "login.html")

    def test_to_delete_a_post_if_logged_in_person_has_no_staff_status(self):
        ''' test delete post when someone is logged in
        with no staff status'''

        # create a user with no staff status
        user = User.objects.create_user(username='username',
                                        email='myemail@test.com',
                                        password='password')
        # login the user
        self.client.login(username='username',
                          password='password')
        # create a post
        post = Post(title="Title",
                    content='content',
                    category='test category',
                    tag='test tag',
                    view_on_front_page='True')
        # save a post
        post.save()
        # delete post url with post id
        page = self.client.get("/posts/{0}/delete/".format(post.id),
                               follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check the template used is index.html
        self.assertTemplateUsed(page, "index.html")
