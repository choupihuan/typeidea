from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post,Tag
# Create your views here.


def post_list(request, category_id=None, tag_id=None):
    if tag_id:
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            post_list = []
        else:
            post_list = tag.post_set.filter(status=Post.STATUS_NORMAL)
    else:
        post_list = Post.objects.filter(status=Post.STATUS_NORMAL)
        if category_id:
            post_list = post_list.filter(category_id=category_id)
    return  render(request,'index.html',context={'post_list':post_list})


def post_detail(request,post_id=None):
    try:
        # tag = Tag.objects.get(id = post_id)
        # post = tag.post_set.filter(id=post_id).first()
        # print(post)
        # post = Post.objects.all().get(id=post_id)
        post = Post.objects.get(id=post_id)
        tag = post.tag.first()
    except Post.DoesNotExist:
        post = None
    return render(request,'detail.html',locals())


