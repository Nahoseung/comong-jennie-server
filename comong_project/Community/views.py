from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Post
from .serializers import PostlistSerializer, PostdetailSerializer


# @api_view(['GET'])
# def post_list(request):
#     posts=Post.objects.all()
#     serializer=PostlistSerializer(posts,many=True)
#     return Response(serializer.data, status=200)


    
# @api_view(['GET'])
# def post_deatil(request,pk):
#     posts_detail=Post.objects.get(id=pk)
#     serializer=PostdetailSerializer(posts_detail) # post object is not iterable
#     return Response(serializer.data, status=200)


class post(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostdetailSerializer
    
    
# post_list에서는 제목,작성자(+프로필),시간,태그만 보이도록(content 제외) 세부 기능 구현
# ModelViewset 조금 더 공부 필요