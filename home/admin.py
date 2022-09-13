from django.contrib import admin
from .models import  Post, Profile, Category
from image_cropping import ImageCroppingMixin
from django.contrib.auth.models import User


# Register your models here.


@admin.register(Post)
class PostAdmin(ImageCroppingMixin,admin.ModelAdmin):
    list_display = ['date','title']


@admin.register(Profile)
class ProfileAdmin(ImageCroppingMixin,admin.ModelAdmin):
    pass


class UserAdmin(User):
    list_display = ['first_name', 'last_name']


admin.site.register(Category)

