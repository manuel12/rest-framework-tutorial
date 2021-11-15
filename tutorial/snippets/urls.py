from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets.views import SnippetViewSet, UserViewSet


# Create a router and register viewsets with it.
router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)
router.register(r'user', UserViewSet)

# The APIs URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls))
]
