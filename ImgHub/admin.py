from django.contrib import admin
from .models import ImageDB
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Account


class ImageDBAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'u_ctg', 'v_ctg','published_on')
    list_filter = ('u_ctg','v_ctg')
    search_fields = ('name', 'u_ctg')
    ordering = ('published_on',)
    filter_horizontal = ()

admin.site.register(ImageDB,ImageDBAdmin)
# admin.site.register(SignUpModel)

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    # form = UserChangeForm
    # add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'username','date_joined','last_login','is_staff','is_admin')
    list_filter = ('is_admin',)
    fieldsets = ()
    search_fields = ('email','username')
    ordering = ('username',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(Account, UserAdmin)