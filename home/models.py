from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_resized import ResizedImageField
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    ocupation = models.CharField(max_length=255, blank=True,null=True)
    bio = models.TextField(max_length=2500)
    picture = ResizedImageField(default='images/profile_images/anonymous.jpg', size=[150, 150], crop=['top', 'left'], upload_to='images/profile_images')
    github_url = models.CharField(max_length=255, blank=True)
    twitter_url = models.CharField(max_length=255, blank=True)
    facebook_url = models.CharField(max_length=255, blank=True)
    instagram_url = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.user)


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = ResizedImageField(size=[1280, 720], crop=['top','left','right'], upload_to='images/category_images', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Post(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank = True)
    category = models.ForeignKey(Category,default= "", on_delete=models.PROTECT, blank=False, null=False )
    content = models.TextField(max_length=2500)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    objects = models.Manager()
    image = ResizedImageField(size=[984, 616], crop=['top','left','right'], upload_to='images/post_images')
    image_font = models.CharField(max_length=255, blank=True)
    references = models.TextField(max_length=2500, blank=True)
    FEATURE_CHOICES = (
        (True, 'Yes'),
        (False, 'No'),
    )
    feature = models.BooleanField(max_length=20, choices=FEATURE_CHOICES, default=False)

    def save(self, *args, **kwargs):
        if self.feature == True:
            Post.objects.filter(feature=True).update(feature=False)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')

