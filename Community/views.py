from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Post
from .serializers import PostlistSerializer, PostdetailSerializer

@api_view(['GET'])
def post_list(request):
    posts=Post.objects.all()
    serializer=PostlistSerializer(posts,many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def post_deatil(request,pk):
    posts_detail=Post.objects.get(id=pk)
    serializer=PostdetailSerializer(posts_detail) # post object is not iterable
    return Response(serializer.data, status=200)