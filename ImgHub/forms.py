from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import ImageDB


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageDB
        fields = ["name", "image_file", 'u_ctg']
        # widgets = {
        #     "image_file": forms.ImageField(attrs={'id': 'blah', 'class': 'input-class_name'}),
        # }


# class SignUpForm(forms.ModelForm):
#     password1 = forms.CharField(max_length=20)
#     class Meta:
#         model = SignUpModel
#         fields = ["username", "firstName", "lastName", "email", "gender", "password"]

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')