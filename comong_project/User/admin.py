from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Tier, User

admin.site.register(Tier)
admin.site.register(User,UserAdmin)
UserAdmin.fieldsets += (("Custom fields",{"fields":("nickname","profile_pic","tier")}),)