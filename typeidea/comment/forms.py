import mistune

from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) <10:
            raise forms.ValidationError('内容必须超过10')
        return content

    class Meta:
        model = Comment
        fields = ['content']