from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django.conf import settings

class ImageDB(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null='Admin')
    u_ctg_options = [('unknown', 'unknown'), ('Animal', 'Animal'), ('Fruit', 'Fruit'), ('Nature', 'Nature'), ('Art', 'Art')]
    name = models.CharField(max_length=500)
    image_file = models.ImageField(upload_to='images/')
    u_ctg = models.CharField(max_length=10, default='unknown', choices=u_ctg_options)
    v_ctg = models.CharField(max_length=10, default="unknown")
    hash_val = models.CharField(max_length=100, null=True)
    published_on=models.DateTimeField(default=timezone.now())
    # hash_val max length <=36

    def __str__(self):
        return self.name + " : " + str(self.image_file)


# class MyUser(AbstractUser):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30, )
#     email = models.EmailField(max_length=254, )
#     mobile = models.IntegerField()
#     pet_name = models.CharField(max_length=10)



class MyAccountManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not username:
            raise ValueError("User must have an username")
        if not email:
            raise ValueError("User must have an email")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        # create superuser here
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    username =            models.CharField(max_length=30, unique=True)
    email =               models.EmailField(max_length=40, unique=True)
    date_joined =         models.DateTimeField(auto_now_add=True)
    last_login =          models.DateTimeField(auto_now=True)
    is_admin =            models.BooleanField(default=False)
    is_staff =            models.BooleanField(default=False)
    is_active =           models.BooleanField(default=True)
    is_superuser =        models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Profile():
    pass


