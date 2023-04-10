from django.shortcuts import render, redirect
from .models import Article 


def new(request):
    # 사용자에게 form이 담긴 html을 보여줌
    return render(request, 'blog/new.html')

def create(request):
    # 새로운 게시글(Article instance)를 생성.
    article = Article()
    article.title = request.POST['title']
    article.content = request.POST['content']
    article.save()

    # return render(request, 'blog/new.html')
    return redirect(f'/blog/{article.pk}')
    # 상세페이지로 redirect 함!!

def index(request):
    # 게시글 목록을 사용자에게 html로 보여줌.
    articles = Article.objects.all()

    return render(request, 'blog/index.html', {
        'articles': articles,
    })
            # article_pk는 variable routing으로 넘어온 값!

def detail(request, article_pk):
    # 게시글 상세 내용을 사용자에게 html로 보여줌
    article = Article.objects.get(pk=article_pk)

    return render(request, 'blog/detail.html', {
        'article': article
    })

def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    
    return render(request, 'blog/edit.html', {
        'article': article
    })


def update(request, article_pk):
    a = Article.objects.get(pk=article_pk)
    a.title = request.POST['title']
    a.content = request.POST['content']
    a.save()

    return redirect(f'/blog/{a.pk}')
    # return redirect(f'/blog/{article_pk}')
    # 둘 다 사용 가능하다!


def delete(request, article_pk):
    # 특정 게시글의 삭제
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('/blog/')
