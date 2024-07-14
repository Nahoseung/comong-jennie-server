from django.contrib import admin
from django.urls import path,include
# from .views import grade,sub,prof,posts,post_detail
from .views import post_list
urlpatterns = [
    # path('grade/', grade),
    # path('sub/',sub),
    # path('prof/',prof),
    path('posts/',post_list),
    # path('sub/<int:post_id>/',post_detail),
]