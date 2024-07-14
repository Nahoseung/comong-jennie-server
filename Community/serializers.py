from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.Serializer):
    class Meta:
        model = Post
        fields=['id','title','content','Date_Created','Date_Modified',] #'author','Tag']
        # read_only_fields=['id','title','content','Date_Created','Date_Modified']
        
