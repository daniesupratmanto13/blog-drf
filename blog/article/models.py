from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# utils
from .utils import profile_pic_path, unique_slugify


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=150, blank=True, null=True)
    bio = models.TextField(max_length=400, blank=True, null=True)
    picture = models.ImageField(
        default='blank-profile.webp', upload_to=profile_pic_path)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.id}_{self.first_name} {self.last_name}'


class Article(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=100, blank=False)
    # body = models.TextField(max_length=1000)
    body = RichTextUploadingField()
    posted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, unique=True)

    __title = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__title = self.title

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs) -> None:
        self.slug = unique_slugify(
            self.title, self.__title, self.slug, Article, 5)
        super().save(*args, **kwargs)

    @property
    def total_likes(self) -> int:
        return self.likesarticle.filter(value='LK').count()

    @property
    def total_comments(self) -> int:
        return self.comments.all().count()


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    comment = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.comment


class LikeUnlikeArticle(models.Model):
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
