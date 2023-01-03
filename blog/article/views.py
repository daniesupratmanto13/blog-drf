from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer

# models
from .models import Article, LikeUnlikeArticle

# serializers
from .serializers import (
    ArticleSerializer,
    CommentPostSerializer,
    LikeArticleSerializer,
    UserSerializer,
)

# Create your views here.


class RegisterViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = User(email=serializer.data.get('email'),
                        username=serializer.data.get('username'))
            user.set_password(request.data.get('passwor'))
            user.save()

            return Response({'message': 'registration success', 'data': serializer.data})


class LoginViewSet(viewsets.ViewSet):
    serializer_class = AuthTokenSerializer

    def create(self, request):
        user = User.objects.filter(username=request.data.get(
            'username'), email=request.data.get('email')).first()

        if user is None:
            return Response({'message': 'login failed', 'data': {}})

        serializer = self.serializer_class(
            data=request.data, context={'request': request})

        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)

            return Response({'message': 'success', 'status': True, 'data': {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'token': token.key
            }})

        return Response({'message': 'login failed', 'data': {}})


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


class CommentCreate(generics.CreateAPIView):
    serializer_class = CommentPostSerializer


class LikeCreate(generics.CreateAPIView):
    serializer_class = LikeArticleSerializer


class LikeUpdate(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView
):
    queryset = LikeUnlikeArticle.objects.all()
    serializer_class = LikeArticleSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class ArticleList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ArticleDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
