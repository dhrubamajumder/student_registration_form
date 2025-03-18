from . models import Book
from django import forms

class BookForms(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['titel','author','discription','published_year']