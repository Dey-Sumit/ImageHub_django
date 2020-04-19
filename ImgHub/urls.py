from django.urls import path
from .views import index,profile

urlpatterns = [
    path('', profile, name='profile'),
]