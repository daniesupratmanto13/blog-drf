from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from rest_framework.urlpatterns import format_suffix_patterns

# views
from . import views

app_name = 'article'

router = DefaultRouter()
router.register(r'register', views.RegisterViewSet, basename="register")
router.register(r'login', views.LoginViewSet, basename="login")

urlpatterns = [
    path('', views.api_root),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('articles/', views.ArticleList.as_view(), name='article-list'),
    path('comments/', views.CommentCreate.as_view(), name='comment-create'),
    path('likes/', views.LikeCreate.as_view(), name='like-create'),
    path('profiles/', views.ProfileList.as_view(), name='profile-list'),
    path('users/<str:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('articles/<str:pk>/', views.ArticleDetail.as_view(), name='article-detail'),
    path('likes/<str:pk>/', views.LikeDetail.as_view(), name='like-update'),
    path('profiles/<str:pk>/', views.ProfileDetail.as_view(), name='profile-detail'),
    path('', include(router.urls)),
    # path('comments/', views.CommentList.as_view(), name='comment-list'),
    # path('comments/<str:pk>/', views.CommentDetail.as_view(), name='comment-detail'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
