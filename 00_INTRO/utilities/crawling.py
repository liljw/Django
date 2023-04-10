# crawling.py
# pip install requests

import requests
from bs4 import BeautifulSoup

def get_real_lotto():
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%A1%9C%EB%98%90'
    # 요청은 클라이언트 프로그램을 통해 URL로 보낸다.
    res = requests.get(url)  # get 메서드는 '내놔!'라는 의미.
    data = BeautifulSoup(res.text, 'html.parser')
    real_numbers = []

    for tag in data.select('.ball'):  # ball 앞에 있는 . 은 class를 의미한다. 
        real_numbers.append(tag.text)

    real_numbers = list(map(int, real_numbers))
    bonus_number = real_numbers.pop()

    # list(map(lambda tag: int(tag.text), data.select('.ball')))  # lambda 이용해서 뽑는 법.

    # return {'real_numbers': real_numbers, 'bonus_number': bonus_number}  # dictionary로 받아서 return함!
    return real_numbers, bonus_number

