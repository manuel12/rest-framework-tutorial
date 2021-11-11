from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions

from snippets.models import Snippet
from snippets.serializers import UserSerializer, SnippetSerializer
from snippets.permissions import IsOwnerOrReadOnly

# Create your views here.

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class  =UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetList(generics.ListCreateAPIView):
    permission_class = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_class = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer