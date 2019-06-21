from django.contrib import admin

# Register your models here.
from .models import Comment
from typeidea.custom_site import custom_site


@admin.register(Comment,site=custom_site)
class Comment(admin.ModelAdmin):
    list_display = ['target','content','nickname','website','create_time']
