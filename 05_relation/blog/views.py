from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_safe, require_http_methods
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count

from .models import Posting, Reply
from .forms import PostingForm, ReplyForm

@login_required  # decorator들 사이의 순서는 중요함!!
@require_http_methods(["GET", "POST"])
def create_posting(request):
    if request.method == 'GET':
        form = PostingForm()
    else:
        form = PostingForm(request.POST)
        if form.is_valid():
            posting = form.save(commit=False)
            posting.user = request.user
            posting.save()
            return redirect('blog:posting_detail', posting.pk)
    
    return render(request, 'blog/form.html', {
        "form": form,
    })

@require_safe
def posting_index(request):

    postings = Posting.objects.annotate(like_count=Count('like_users')).order_by('-like_count')

    paginator = Paginator(postings, 10) # Show 10 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    return render(request, 'blog/index.html', {
        # "postings": postings,
        "page_obj": page_obj
    })

@require_safe
def posting_detail(request, posting_pk):
    posting = get_object_or_404(Posting, pk=posting_pk)
    # 댓글 index도 posting_detail 에서 진행
    # 특정 게시글 (위에서 가지고온 posting)의 댓글들만 다 가져옴!
    replies = posting.reply_set.all()
    # 댓글 create도 posting_detail 에서 진행
    form = ReplyForm()

    is_like = posting.like_users.filter(pk=request.user.pk).exists()

    return render(request, 'blog/detail.html', {
        "posting": posting,
        "replies": replies,
        "form": form,
        "is_like": is_like,
    })

@login_required
@require_http_methods(["GET", "POST"])
def update_posting(request, posting_pk):
    posting = get_object_or_404(Posting, pk=posting_pk)

    # 요청보낸 사용자가 posting을 작성한 사람이 아니라면, 못하게 함!
    if request.user != posting.user:
        return redirect('blog:posting_index')
    
    if request.method == "GET":
        form = PostingForm(instance=posting)
    else:
        form = PostingForm(request.POST, instance=posting)
        if form.is_valid():
            posting = form.save()
            return redirect('blog:posting_detail', posting.pk)
    return render(request, 'blog/form.html', {
        "form": form,
    })

@login_required
@require_POST
def delete_posting(request, posting_pk):
    posting = get_object_or_404(Posting, pk=posting_pk)

    if request.user != posting.user:
        return redirect('blog:posting_index')
    
    posting.delete()
    return redirect('blog:posting_index')

@login_required 
@require_POST
def create_reply(request, posting_pk):
    posting = get_object_or_404(Posting, pk=posting_pk)
    form = ReplyForm(request.POST)

    if form.is_valid():
        reply = form.save(commit=False)
        reply.posting = posting
        reply.user = request.user
        reply.save()
        return redirect('blog:posting_detail', posting_pk)
    '''
    else:
        from django.http import HttpResponseBadRequest
        return HttpResponseBadRequest('댓글 에러')

        return render(request, 'blog/detail.html', {
            "form": form,
            "posting": p,
            "replies": p.reply_set.all(),
        })
    '''

@login_required
@require_POST
def delete_reply(request, posting_pk, reply_pk):
    posting = get_object_or_404(Posting, pk=posting_pk)
    reply = get_object_or_404(Reply, pk=reply_pk)

    if request.user != reply.user:
        return redirect('blog:posting_index')
    
    reply.delete()
    return redirect('blog:posting_detail', posting.pk)

@login_required
@require_POST
def like_posting(request, posting_pk):
    posting = get_object_or_404(Posting, pk=posting_pk)
    user = request.user
    # 기존 사용자들 목록에 있으면 좋아요를 '취소'한다.
    # if user in posting.like_users.all():
    if posting.like_users.filter(pk=user.pk).exists():
        posting.like_users.remove(user)
    else:
        posting.like_users.add(user)
    return redirect('blog:posting_detail', posting.pk)

@login_required
@require_safe
def feed(request):
    user = request.user
    # Posting 객체들 중에 user(작성자)가 user.stars.all()
    # postings = Posting.objects.filter(user__in=user.stars.all())
    stars_postings = []
    for star in user.stars.all():
        for posting in star.posting_set.all():
            stars_postings.append(posting)
    return render(request, 'blog/feed.html', {
        # 'postings': postings,
        'stars_postings': stars_postings
    })

