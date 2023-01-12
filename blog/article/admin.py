from django.contrib import admin

# models
from .models import Article, Comment, LikeUnlikeArticle, Profile

# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(LikeUnlikeArticle)
admin.site.register(Profile)
