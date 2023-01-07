from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

# views
from . import views

app_name = 'article'

urlpatterns = [
    path('', views.api_root),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('articles/', views.ArticleList.as_view(), name='article-list'),
    path('comments/', views.CommentCreate.as_view(), name='comment-create'),
    path('likes/', views.LikeDetail.as_view(), name='like-create'),
    # path('comments/', views.CommentList.as_view(), name='comment-list'),
    path('users/<str:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('articles/<str:pk>/', views.ArticleDetail.as_view(), name='article-detail'),
    path('likes/<str:pk>/', views.LikeUpdate.as_view(), name='like-update'),
    # path('comments/<str:pk>/', views.CommentDetail.as_view(), name='comment-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
