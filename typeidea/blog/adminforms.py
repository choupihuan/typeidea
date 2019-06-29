from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from dal import autocomplete


from .models import Post,Category,Tag



class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea,label='摘要',required=False)
    # category = forms.ModelChoiceField(
    #     queryset=Category.objects.all(),
    #     widget=autocomplete.ModelSelect2(url='category-autocomplete'),
    #     label='分类',
    # )
    # tag = forms.ModelChoiceField(
    #     queryset=Tag.objects.all(),
    #     widget=autocomplete.ModelSelect2(url='tag-autocomplete'),
    #     label='标签',
    # )



    """
    警告：出现懒加载修改信息出错,已解决，出现原因应该是由于懒加载和ckeditor同时存在，以及布置的位置有问题导致的加载不能修改信息，解决方案，用另外一种懒加载书写方式
    """
    content_ck = forms.CharField(widget=CKEditorUploadingWidget(),label='正文',required=False)
    content_md = forms.CharField(widget=CKEditorUploadingWidget(),label='正文',required=False)
    content = forms.CharField(widget=forms.HiddenInput(),required=False)


    class Meta:
        model = Post
        fields = ('category','tag','desc','title','is_md','content','status','content_md','content_ck')
        widgets = {
            'category':autocomplete.ModelSelect2(url='category-autocomplete'),
            'tag':autocomplete.ModelSelect2(url='tag-autocomplete'),
        }


    def __init__(self,instance=None,initial=None,**kwargs):
        initial = initial or {}
        if instance:
            if instance.is_md:
                initial['content_md'] = instance.content
            else:
                initial['content_ck'] = instance.content

        super().__init__(instance=instance,initial=initial,**kwargs)

    def clean(self):
        is_md = self.cleaned_data.get('is_md')
        if is_md:
            content_field_name = 'content_md'
        else:
            content_field_name = 'content_ck'
        content = self.cleaned_data.get(content_field_name)
        if not content:
            self.add_error(content_field_name,'必填项')
            return
        self.cleaned_data['content'] = content
        return super().clean()

    class Media:
        js = ('js/post_editor.js',)