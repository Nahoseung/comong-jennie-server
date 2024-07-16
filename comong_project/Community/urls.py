from django.contrib import admin
from django.urls import path,include
# from .views import grade,sub,prof,posts,post_detail
from .views import post_list, post_deatil
urlpatterns = [
    # path('grade/', grade),
    # path('sub/',sub),
    # path('prof/',prof),
    path('posts/',post_list),
    path('posts/<int:pk>/', post_deatil),
]