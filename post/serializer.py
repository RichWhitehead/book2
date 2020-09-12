from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
  fields = ('id', 'author', 'title', 'created_at')
  model = Post