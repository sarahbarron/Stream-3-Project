from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    ''' form to leave a product review '''

    class Meta:
        # form is based on the Reviw Model
        model = Review
        # fileds to be used in the form
        fields = ('title',
                  'comment',
                  'rating',
                  'would_you_recommend_to_a_friend')
