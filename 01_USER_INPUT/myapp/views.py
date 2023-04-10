from django.shortcuts import render
import requests

# name => variable routing
def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'myapp/hello.html')

# ping 함수를 실행하는 방법은? 단 한가지 밖에 없다! myapp/ping/ 의 url로 접근하는 것!
def ping(request):
    return render(request, 'myapp/ping.html')

def pong(request):
    # 이미 사용자 입력은 request 안에 도달함!!
    # POST 방식
    # 1. <form method="POST">
    # 2. <form> > {% csrf_token %}
    # 3. view => request.POST
    context = {
        'name': request.POST["myname"],
        'age': request.POST["age"],
        'mbti': request.POST["mbti"],
    }    
    return render(request, 'myapp/pong.html', context)

def lotto_in(request):
    return render(request, 'myapp/lotto_in.html')

def lotto_out(request):
    drwno =  request.GET["drwno"]
    my_url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={int(drwno)}'

    res = requests.get(my_url).json()
    real_numbers = []
    for k, v in res.items():
      if 'drwtNo' in k:
          real_numbers.append(v)
    # list comprehension 으로 쓰면
    # numbers = [value for key, value in res.items() if 'drwtNo' in key]

    real_numbers = set(real_numbers)
    my_numbers = list(map(int, request.GET["my_numbers"].split()))
    my_numbers = set(my_numbers)
    my_bonus_number = request.GET["my_bonus_number"]

    intersection_number = list(my_numbers & real_numbers)

    if len(intersection_number) == 6:
        result =  "1등"
    elif len(intersection_number) == 5:
        if int(my_bonus_number) == res['bnusNo']:
            result = "2등"
        else:
            result = "3등"
    elif len(intersection_number) == 4:
        result = "4등"
    elif len(intersection_number) == 3:
        result = "5등"
    else:
        result = "꽝"

    context = {
        'real_numbers': real_numbers,
        'bonus_number': res['bnusNo'],
        'result': result,
    }
    return render(request, 'myapp/lotto_out.html', context)