from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename = 'category')

urlpatterns = [
    path('list-articles/', ArticleList.as_view(),  name = 'article-list'),
    path('create-article/', ArticleCreate.as_view(), name = 'article-create'),
    path('retrieve-article/', ArticleRetrieve.as_view(), name = 'article-retrieve'),
    path('update-article', ArticleUpdate.as_view(), name = 'article-update'),
    path('delete-article', ArticleDelete.as_view(), name = 'article-delete'),
    path('', include(router.urls))
]