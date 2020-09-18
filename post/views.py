from django.shortcuts import render
from rest_framework import generics
from .serializer import PostSerializer
from .models import Post
from .permissions import IsAuthorOrReadOnly


# Create your views here.


class PostList(generics.ListCreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsAuthorOrReadOnly,)
  query = Post.objects.all()
  serializer_class = PostSerializer
