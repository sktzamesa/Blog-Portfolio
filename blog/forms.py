from django import forms
from .models import Comment
class EmailPostForms(forms.Form):
    name = forms.CharField(
        max_length=25,
        label="Your Name",
        widget=forms.TextInput(attrs={
            'class': 'w-full p-2 border rounded',
            'placeholder': 'Enter your name',
        })
    )
    email = forms.EmailField(
        label="Your Email",
        widget=forms.EmailInput(attrs={
            'class': 'w-full p-2 border rounded',
            'placeholder': 'Enter your email',
        })
    )
    to = forms.EmailField(
        label="Recipient's Email",
        widget=forms.EmailInput(attrs={
            'class': 'w-full p-2 border rounded',
            'placeholder': 'Enter recipient’s email',
        })
    )
    comment = forms.CharField(
        required=False,
        label="Comment",
        widget=forms.Textarea(attrs={
            'class': 'w-full p-2 border rounded',
            'placeholder': 'Add a comment (optional)',
            'rows': 4,
        })
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

