from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseBadRequest
from django.contrib.auth import login, logout, get_user_model
# settings.py 의 AUTH_USER_MODEL 값을 설정해준 것 때문에 get_user_model을 해도 알아서 django가 찾아서 가져와 줌!

from .forms import CustomUserCreationForm

User = get_user_model()

@require_http_methods(["GET", "POST"])
def signup(request):
    if request.user.is_authenticated:
        return redirect('blog:posting_index')
    # create_user
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # 새로운 사용자 생성
            # 회원가입을 하면 자동적으로 로그인이 되게끔 하는 법
            login(request, user)
            return redirect('blog:posting_index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {
        "form": form
    })

@require_http_methods(["GET", "POST"])
def signin(request):
    # 로그인이 되어있으면 여기로 오면 안됨! 튕겨내기.
    if request.user.is_authenticated:
        return redirect('blog:posting_index')
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        # ID/PW가 맞다면,
        if form.is_valid():
            # AuthenticationForm은 용도가 다르기 때문에, .get_user() 메서드가 존재
            user = form.get_user()  # id/pw로 찾은 기존 사용자
            # 인증 => 쿠키에 정보 저장
            login(request, user)  # 기존 사용자로 로그인(set cookie)

            # 0. URL에 ?와 &로 넘어오는 값들은 모두 request.GET 꾸러미에 담긴다.
            # 1. request.GET은 dict
            # 2. dict의 get 메서드 떠올리기
            # 3. or 은 1 or 2 or 3 / 0 or 1 or 2
            return redirect(request.GET.get('next') or 'blog:posting_index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/signin.html', {
        "form": form
    })

def signout(request):
    logout(request)
    return redirect('blog:posting_index')

@require_safe
def profile(request, username):
    # username(컬럼명) = username(var routing 변수명)
    # 변수명을 그냥 user 라고 써주면, 나중에 request.user를 쓴다던가 할 때 헷갈릴 수 있다!
    profile_user = get_object_or_404(User, username=username)

    is_follow = profile_user.fans.filter(pk=request.user.pk).exists()

    is_notme = profile_user != request.user

    return render(request, 'accounts/profile.html', {
        'profile_user': profile_user,
        'is_follow': is_follow,
        'is_notme': is_notme,
    })

@require_POST
def follow(request, username):
    profile_user = get_object_or_404(User, username=username)
    user = request.user

    if profile_user == user:
        return HttpResponseBadRequest('Can not follow yourself')

    if user in profile_user.fans.all():
        profile_user.fans.remove(user)
    else:
        profile_user.fans.add(user)
    
    return redirect('accounts:profile', profile_user.username)