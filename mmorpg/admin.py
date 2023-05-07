from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from mmorpg.models import Post, Profile, Category


admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Category)
