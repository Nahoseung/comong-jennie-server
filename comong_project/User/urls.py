from django.urls import path, include
from . import views
from rest_framework import urls

urlpatterns = [
    path("",views.index,name="index"),
    path("users/<int:user_id>/",views.ProfileView.as_view(),name="profile"),
    path('signup/', views.UserCreate.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]