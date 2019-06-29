import xadmin

from django.contrib import admin

# Register your models here.
from .models import Comment
from typeidea.custom_site import custom_site


@xadmin.sites.register(Comment)
class Comment(object):
    list_display = ['target','content','create_time']
