# Generated by Django 3.2.15 on 2022-09-13 08:38

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=['top', 'left', 'right'], force_format=None, keep_meta=True, quality=-1, scale=None, size=[1280, 720], upload_to='images/category_images')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='UserAdmin',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocupation', models.CharField(blank=True, max_length=255, null=True)),
                ('bio', models.TextField(max_length=2500)),
                ('picture', django_resized.forms.ResizedImageField(crop=['top', 'left'], default='images/profile_images/anonymous.jpg', force_format=None, keep_meta=True, quality=-1, scale=None, size=[150, 150], upload_to='images/profile_images')),
                ('github_url', models.CharField(blank=True, max_length=255)),
                ('twitter_url', models.CharField(blank=True, max_length=255)),
                ('facebook_url', models.CharField(blank=True, max_length=255)),
                ('instagram_url', models.CharField(blank=True, max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(blank=True, max_length=255)),
                ('content', models.TextField(max_length=2500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', django_resized.forms.ResizedImageField(crop=['top', 'left', 'right'], force_format=None, keep_meta=True, quality=-1, scale=None, size=[984, 616], upload_to='images/post_images')),
                ('image_font', models.CharField(blank=True, max_length=255)),
                ('references', models.TextField(blank=True, max_length=2500)),
                ('feature', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, max_length=20)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='home.category')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]