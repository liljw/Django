from django import forms
from .models import Article, Reply

class ArticleForm(forms.ModelForm):
    title = forms.CharField(min_length=5, max_length=30)
    content = forms.CharField()

    class Meta:
        model = Article
        exclude = ('user', )

class ReplyForm(forms.ModelForm):

    class Meta:
        model = Reply
        fields = ('content', )
    
