from datetime import date

from django.shortcuts import render
from django.views.generic import DetailView,ListView
from django.shortcuts import get_object_or_404
from django.db.models import Q,F
from django.core.cache import cache

from .models import Post,Tag,Category
from .adminforms import PostAdminForm
from config.models import SideBar,Link
from comment.forms import CommentForm
# Create your views here.


class CommonViewMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'sidebars':SideBar.get_all(),
                        'categorys': Category.get_navs(),
                        'hot_posts': Post.hot_posts()[:6],
                        'new_posts': Post.new_posts()[:6],
                        'tags':Tag.latest_posta(),
                        'links':Link.show_list(),
                        'refer_post':Post.latest_posta()[:6],
                        'comment_form': CommentForm(),
                        'publish': PostAdminForm(),
                        })
        return context


class IndexView(CommonViewMixin,ListView):
    queryset = Post.latest_posta()
    paginate_by = 5
    model = Post
    context_object_name = 'post_list'
    template_name = 'index.html'


class CategoryView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        category = get_object_or_404(Category,pk=category_id)
        context.update({
            'category':category,
        })
        return context

    def get_queryset(self):
        """重写queryset,根据分类过滤"""
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id)


class TagView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')
        tag = get_object_or_404(Tag,pk=tag_id)
        context.update({
            'tag':tag,
        })
        return context

    def get_queryset(self):
        """重写queryset"""
        queryset = super().get_queryset()
        tag_id = self.kwargs.get('tag_id')
        # 多对多关系，直接调用这个字段的属性名等于某一个id，查询时会自动调用中间表，得到对应的对象
        return queryset.filter(tag=tag_id)


class SearchView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'keyword':self.request.GET.get('keyword','')
        })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.GET.get('keyword')
        if not keyword:
            return queryset
        return queryset.filter(Q(title__icontains=keyword)| Q(desc__icontains=keyword))


class AuthorView(IndexView):
    def get_queryset(self):
        queryset = super().get_queryset()
        author_id = self.kwargs.get('owner_id')
        return queryset.filter(owner_id=author_id)


class PostDetailView(CommonViewMixin,DetailView):
    queryset = Post.latest_posta()
    template_name = 'detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'


    def get(self, request, *args, **kwargs):
        response = super().get(request,*args,**kwargs)
        self.handle_visited()
        return response

    def handle_visited(self):
        increase_pv = False
        increase_uv = False
        uid = self.request.uid
        pv_key = 'pv:%s : %s '%(uid,self.request.path)
        uv_key = 'uv:%s : %s :%s'%(uid,str(date.today()),self.request.path)
        if not cache.get(pv_key):
            increase_pv = True
            cache.set(pv_key,1,1*60)

        if not cache.get(uv_key):
            increase_uv = True
            cache.set(uv_key,1,2*60)

        if increase_uv and increase_pv:
            Post.objects.filter(pk=self.object.id).update(pv=F('pv') + 1,uv=F('uv') + 1)
        elif increase_pv:
            Post.objects.filter(pk=self.object.id).update(pv=F('pv') + 1)
        elif increase_uv:
            Post.objects.filter(pk=self.object.id).update(uv=F('uv') + 1)


def publish(request):
    publish = PostAdminForm()
    return render(request,'publish.html',locals())