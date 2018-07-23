from django.test import TestCase
from .forms import ReviewForm

class Test_Review_Form(TestCase):

    def test_a_valid_review_form(self):
        form = ReviewForm({'title': 'test title', 'comment': 'test content', 'rating': '5', 'would_you_recommend_to_a_friend': 'YES', })
        self.assertTrue(form.is_valid())
    
    def test_an_invalid_review_form_no_title(self):
        form = ReviewForm({'title': '', 'comment': 'test content', 'rating': '5', 'would_you_recommend_to_a_friend': 'YES', })
        self.assertFalse(form.is_valid())
    
    def test_an_invalid_review_form_no_comment(self):
        form = ReviewForm({'title': 'test title', 'comment': '', 'rating': '5', 'would_you_recommend_to_a_friend': 'YES', })
        self.assertFalse(form.is_valid())
    
    def test_an_invalid_review_form_no_rating(self):
        form = ReviewForm({'title': 'test title', 'comment': 'test content', 'rating': '', 'would_you_recommend_to_a_friend': 'YES', })
        self.assertFalse(form.is_valid())
    
    def test_an_invalid_review_form_no_would_you_recommend_to_a_friend_included(self):
        form = ReviewForm({'title': 'test title', 'comment': 'test content', 'rating': '5', 'would_you_recommend_to_a_friend': '', })
        self.assertFalse(form.is_valid())