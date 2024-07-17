'''
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView
from allauth.account.views import PasswordChangeView
from User.models import User

# Create your views here.
def index(request):
    return render(request,"User/index.html")

class ProfileView(DetailView):
    model = User
    template_name = "User/profile.html"
    pk_url_kwarg = "user_id"
    context_object_name = "profile_user"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs.get("user_id")
        context["user_reviews"] = Review.objects.filter(author__id).order_by("-dt_created")[:4]
        return context

class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse("index")
'''
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from allauth.account.views import PasswordChangeView
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import DetailView

# DRF 뷰셋
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# 기존 Django 뷰
def index(request):
    return render(request, "User/index.html")

class ProfileView(DetailView):
    model = User
    template_name = "User/profile.html"
    pk_url_kwarg = "user_id"
    context_object_name = "profile_user"

class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse("index")
