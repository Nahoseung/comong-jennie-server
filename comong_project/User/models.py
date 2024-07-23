from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_no_special_characters

class Tier(models.Model):
    name = models.CharField(max_length=100)
    level = models.PositiveIntegerField(unique=True)  # 티어의 레벨, 높은 숫자가 높은 티어
    benefits = models.TextField(blank=True)  # 티어 혜택 설명

    def __str__(self):
        return self.name


class User(AbstractUser):
    nickname = models.CharField(
        max_length=15,
        unique=True, 
        null= True,
        validators=[validate_no_special_characters],
        error_messages= {"unique": "이미 사용중인 닉네임입니다."},                      
    )

    profile_pic = models.ImageField(
        default = "default_profile_pic.jpg", upload_to="profile_pics"
    ) 

    tier = models.ForeignKey(Tier, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.email