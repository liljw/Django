from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Article, Reply
from .forms import ArticleForm, ReplyForm

# def new(request):
#     form = ArticleForm()
#     return render(request, 'blog/new.html', {
#         "form": form
#     })

# def create(request):
#     form = ArticleForm(request.POST)

#     if form.is_valid():
#         form.save()
#         return redirect("/blog/")
#     else:
#         return render(request, 'blog/new.html', {
#             "form": form
#         })

@login_required
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == 'GET':
        form = ArticleForm()
    
    elif request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('blog:detail', article.pk)

    return render(request, 'blog/form.html', {
        "form": form
    })

@require_safe
def index(request):
    articles = Article.objects.order_by('-updated_at')
    return render(request, 'blog/index.html', {
        "articles": articles
    })

@require_safe
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    replies = article.reply_set.all()
    form = ReplyForm()
    is_like = article.like_users.filter(pk=request.user.pk).exists()
    return render(request, 'blog/detail.html', {
        "article": article,
        "replies": replies,
        "form": form,
        "is_like": is_like,

    })

# def edit(request, article_pk):
#     article = Article.objects.get(pk=article_pk)
#     return render(request, 'blog/edit.html', {
#         "article": article
#     })

# def update(request, article_pk):
#     article = Article.objects.get(pk=article_pk)
#     article.title = request.POST["title"]
#     article.content = request.POST["content"]
#     article.save()

#     return redirect(f'/blog/{article.pk}')

@login_required
@require_http_methods(["GET", "POST"])
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        form = ArticleForm(instance=article)
    else:
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('blog:detail', article.pk)
    return render(request, 'blog/form.html', {
        "form": form
    })

@login_required
@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('blog:index')

@login_required
@require_POST
def create_reply(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    form = ReplyForm(request.POST)
    if form.is_valid():
        reply = form.save(commit=False)
        reply.article = article
        reply.user = request.user
        reply.save()
        return redirect('blog:detail', article.pk)

@login_required
@require_POST
def delete_reply(request, article_pk, reply_pk):
    article = get_object_or_404(Article, pk=article_pk)
    reply = get_object_or_404(Reply, pk=reply_pk)
    reply.delete()
    return redirect('blog:detail', article.pk)

@login_required
@require_POST
def like_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    user = request.user
    if article.like_users.filter(pk=user.pk).exists():
        article.like_users.remove(user)
    else:
        article.like_users.add(user)
    return redirect('blog:detail', article.pk)

