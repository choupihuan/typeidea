"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import xadmin
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

from config.views import links
from blog.views import (
    IndexView,CategoryView,TagView,
    PostDetailView,SearchView,AuthorView,publish
)
from comment.views import CommentView
from .autocomplete import CategoryAutocomplet,TagAutocomplete,PostAutocomplete
from blog.apis import PostViewSet

router = DefaultRouter()
router.register(r'post',PostViewSet,base_name='api-post')

urlpatterns = [
    url(r'^$',IndexView.as_view(),name='index'),
    url(r'^category/(?P<category_id>\d+)/$',CategoryView.as_view(),name='category_list'),
    url(r'^tag/(?P<tag_id>\d+)/$',TagView.as_view(),name='tag_list'),
    url(r'^post/(?P<post_id>\d+).html$',PostDetailView.as_view(),name='post_detail'),
    url(r'^search/$',SearchView.as_view(),name='search'),
    url(r'^author/(?P<owner_id>\d+)$',AuthorView.as_view(),name='author'),
    url(r'^link/$',links,name='links'),
    url(r'^comment/$',CommentView.as_view(),name='comment'),
    url(r'^category-autocomplete/$',CategoryAutocomplet.as_view(),name='category-autocomplete'),
    url(r'^tag-autocomplete/$',TagAutocomplete.as_view(),name='tag-autocomplete'),
    url(r'^post-autocomplete/$',PostAutocomplete.as_view(),name='post-autocomplete'),
    url(r'^super_admin/', admin.site.urls,name='super_admin'),
    url(r'^admin/',xadmin.site.urls,name='xadmin'),
    url(r'^publish/$',publish,name='publish'),
    url(r'^ckeditor/',include('ckeditor_uploader.urls')),
    url(r'^api/',include(router.urls)),
    url(r'^api/docs/',include_docs_urls(title='typeidea apis')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
