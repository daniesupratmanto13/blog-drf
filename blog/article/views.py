from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# models
from .models import Article, Comment

# serializers
from .serializers import ArticleSerializer, CommentReadSerializer, UserSerializer

# Create your views here.


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('article:user-list', request=request, format=format),
        'articles': reverse('article:article-list', request=request, format=format)
    }
    )


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


# class CommentList(generics.ListAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentReadSerializer


# class CommentDetail(generics.RetrieveAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentReadSerializer
