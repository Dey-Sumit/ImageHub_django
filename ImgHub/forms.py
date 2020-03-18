from django import forms
from .models import ImageDB


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageDB
        fields = ["name", "image_file", 'category']
        # widgets = {
        #     "image_file": forms.ImageField(attrs={'id': 'blah', 'class': 'input-class_name'}),
        # }