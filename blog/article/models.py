from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

# Create your models here.


class Article(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    posted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    comment = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.comment


class LikeArticle(models.Model):
    LIKE = 'LK'
    UNLIKE = 'UL'
    LIKE_CHOICES = [
        (LIKE, 'Like'),
        (UNLIKE, 'Unlike')
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='likesuser')
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='likesarticle')
    value = models.CharField(
        max_length=2,
        choices=LIKE_CHOICES,
        default=LIKE
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user}-{self.value}-{self.article}"
