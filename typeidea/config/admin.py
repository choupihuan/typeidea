from django.contrib import admin

# Register your models here.

from .models import Link,SideBar
from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin


@admin.register(Link,site=custom_site)
class LinkAdmin(BaseOwnerAdmin):
    list_display = ['title','href','owner','create_time']
    fields = ['title','href','status','weight']


@admin.register(SideBar,site=custom_site)
class SideBarAdmin(BaseOwnerAdmin):
    list_display = ['title','display_type','status','create_time']
    fields = ['title','display_time','content','status']

