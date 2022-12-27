from django.contrib.auth.models import User
from rest_framework import serializers

# models
from .models import Article, Comment, LikeArticle


class UserSerializer(serializers.HyperlinkedModelSerializer):
    articles = serializers.HyperlinkedRelatedField(
        many=True, view_name='article:article-detail', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'articles']


class CommentSerializer(serializers.ModelSerializer):
    article = serializers.ReadOnlyField(source='article.slug')
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['article', 'author', 'comment', 'created']


class LikeArticleSerializer(serializers.ModelSerializer):
    article = serializers.ReadOnlyField(source='article.slug')
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = LikeArticle
        fields = ['article', 'user', 'value', 'created']


class LikeInArticleSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = LikeArticle
        fields = ['user', 'value', 'created']


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    likesarticle = LikeInArticleSerializer(many=True, read_only=True)

    def get_likesarticle(self, obj):
        return obj.username

    class Meta:
        model = Article
        fields = ['url', 'id', 'author', 'title', 'body',
                  'posted', 'updated', 'slug', 'likesarticle', 'comments']
        extra_kwargs = {
            'url': {'view_name': 'article:article-detail'},
            'author': {'view_name': 'article:user-detail'}
        }
