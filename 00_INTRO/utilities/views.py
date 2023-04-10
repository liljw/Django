from django.shortcuts import render
from django.http import HttpResponse
import random
import requests
from bs4 import BeautifulSoup
from . import crawling
from . import lotto

def get_lotto(request):
    lucky_numbers = random.sample(range(1, 46), 6)
    context = {
        'lucky_numbers': lucky_numbers
    }
    return render(request, 'utilities/lucky_numbers.html', context)

# def this_week(request):
#     URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1059'
#     res = requests.get(url).json()
    # real_numbers = []
    # for k, v in res.items():
    #   if 'drwtNo' in k:
    #       real_numbers.append(v)
    # real_numbers.sort()
    # context = {
    #     'real_numbers': real_numbers,
    #     'bonus_number': res['bnusNo']
    # }
#     return render(request, 'utilities/drw_numbers.html', context)

def this_week(request):
    a, b = crawling.get_real_lotto()
    drw_numbers = a
    bonus_number = b 
    context = {
        'drw_numbers': drw_numbers,
        'bonus_number': bonus_number
    }
    return render(request, 'utilities/drw_numbers.html', context)

def check_lotto(request):
    # lucky_numbers = random.sample(range(1, 46), 6)
    # real_numbers = crawling.get_real_lotto()
    result = lotto.lotto()
    context = {
        # 'lucky_numbers': lucky_numbers,
        # 'real_numbers': real_numbers,
        'result': result
    }
    return render(request, 'utilities/result.html', context)