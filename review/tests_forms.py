from django.test import TestCase
from .forms import ReviewForm


class Test_Review_Form(TestCase):
    ''' test the review form '''

    def test_a_valid_review_form(self):
        ''' test a valid review form '''

        # create a form with all valid fields
        form = ReviewForm({'title': 'test title',
                           'comment': 'test content',
                           'rating': '5',
                           'would_you_recommend_to_a_friend': 'YES'})
        # test the form is valid
        self.assertTrue(form.is_valid())

    def test_an_invalid_review_form_no_title(self):
        ''' test the review with no title '''

        # create a form with no title
        form = ReviewForm({'title': '',
                           'comment': 'test content',
                           'rating': '5',
                           'would_you_recommend_to_a_friend': 'YES'})
        # test the form is not valid without a title
        self.assertFalse(form.is_valid())

    def test_an_invalid_review_form_no_comment(self):
        ''' test the review form with no comment '''

        # create a form with no comment
        form = ReviewForm({'title': 'test title',
                           'comment': '',
                           'rating': '5',
                           'would_you_recommend_to_a_friend': 'YES'})
        # test the form is not valid with no comment
        self.assertFalse(form.is_valid())

    def test_an_invalid_review_form_no_rating(self):
        ''' test the review form with no rating '''
        # create a form with no rating
        form = ReviewForm({'title': 'test title',
                           'comment': 'test content',
                           'rating': '',
                           'would_you_recommend_to_a_friend': 'YES'})
        # check the form is not valid with no rating
        self.assertFalse(form.is_valid())

    def test_an_invalid_review_form_no_recommend_to_a_friend_included(self):
        ''' test the form with no would you recommend to a friend '''

        # creaate a form with no would you recommend to a friend
        form = ReviewForm({'title': 'test title',
                           'comment': 'test content',
                           'rating': '5',
                           'would_you_recommend_to_a_friend': ''})
        # check the form is not valid without
        # a would you recommend to a friend input
        self.assertFalse(form.is_valid())
