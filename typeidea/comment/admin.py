from django.contrib import admin

# Register your models here.
from .models import Comment


@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = ['target','content','nickname','website','create_time']
