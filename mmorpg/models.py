from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='media/profile_photos', null=True, blank=True)
    telegram = models.CharField('Telegram', max_length=32, default='no telegram')
    discord = models.CharField('Discord', max_length=32, default='no discord')
    about_me = RichTextUploadingField()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField('Category name', max_length=16, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ManyToManyField("Category", through='PostCategory',)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = RichTextUploadingField()

    def __str__(self):
        return self.title


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
