from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        # ['id','title','content','Created','Modified',] #'author','Tag']
        # read_only_fields=['id','title','content','Date_Created','Date_Modified']
        
