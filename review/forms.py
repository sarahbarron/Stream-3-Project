from django import forms
from .models import Review

# Form to leave a product review
class ReviewForm(forms.ModelForm):
    
    class Meta:
        # form is based on the Reviw Model
        model = Review
        
        # fileds to be used in the form
        fields = ('title', 'comment', 'rating','would_you_recommend_to_a_friend')
    