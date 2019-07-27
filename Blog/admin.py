from django.contrib import admin
from . models import BlogApp, Comment

admin.site.register(BlogApp)
admin.site.register(Comment)