from django.contrib import admin

# models
from .models import Article, Comment, LikeArticle

# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(LikeArticle)
