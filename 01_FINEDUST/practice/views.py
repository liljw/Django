from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def get_info(request):
    URL = 'https://weather.naver.com/air/09680106'
    res = requests.get(URL)
    data = BeautifulSoup(res.text, 'html.parser')
    area = []

    for tag in data.select('.area_position'):
        area.append(tag.text)
    
    context = {
        'area': area
    }
    
    return render(request, 'practice/get_info.html', context)
