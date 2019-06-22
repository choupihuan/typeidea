from django.shortcuts import render

from .models import Post,Tag,Category
from config.models import SideBar
# Create your views here.


def post_list(request, category_id=None, tag_id=None):
    category = None
    tag = None
    if tag_id:
        post_list,tag = Post.get_by_tag(tag_id)
    elif category_id:
        post_list,category = Post.get_by_category(category_id)
    else:
        post_list = Post.latest_posta()

    context = Category.get_navs()
    sidebars = SideBar.get_all()
    return  render(request,'blog/list.html',locals())


def post_detail(request,post_id=None):
    post_list = Post.latest_posta()


    return render(request,'detail.html',locals())


def index(request):
    post_list = Post.latest_posta()
    categories = Category.objects.all()
    return render(request,'index.html',locals())