from django import forms
from .models import Comment
class EmailPostForms(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comment = forms.CharField(
        required=False,
        widget=forms.Textarea
    )
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','body']

class SearchForm(forms.Form):
    query = forms.CharField()

class ContactForm(forms.Form):
    name = forms.CharField(max_length=250)
    email = forms.EmailField()
    phone = forms.CharField(max_length=25)
    message = forms.CharField(
        required=False,
        widget=forms.Textarea
    )

