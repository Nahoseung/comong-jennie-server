from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
# from .views import grade,sub,prof,posts,post_detail
from .views import post

router = DefaultRouter()
router.register('post', post)  

# router url 종류 파악 필요

urlpatterns = [
    path('', include(router.urls)),
    # path('grade/', grade),
    # path('sub/',sub),
    # path('prof/',prof),
    # path('posts/',post_list),
    # path('posts/<int:pk>/', post_deatil),
]