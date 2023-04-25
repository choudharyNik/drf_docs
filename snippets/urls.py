from snippets import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from django.http import JsonResponse


router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
