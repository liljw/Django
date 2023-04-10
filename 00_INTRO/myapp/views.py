# myapp/views.py

from django.shortcuts import render
from django.http import HttpResponse
import random

# view는 function(함수)이다!

def hello(request):
    lucky_numbers = random.sample(range(1, 46), 6)
    return HttpResponse(' '.join(map(str, lucky_numbers)))

def bye(request):
    return HttpResponse('Goodbye My Friend!')

def review(request):
    return render(request, 'review.html')

def index(request):
    lucky_numbers = random.sample(range(1, 46), 6)
    context = {
        'lucky_numbers': lucky_numbers,
    }
    return render(request, 'myapp/index.html', context)