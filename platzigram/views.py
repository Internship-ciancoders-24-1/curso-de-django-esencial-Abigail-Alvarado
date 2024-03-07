from django.http import HttpResponse
from datetime import datetime
from django.http import JsonResponse
import pdb
import json

def hello(request):
    now = datetime.now().strftime('%b %dth, %y - %H:%M hrs')
    return HttpResponse('oh, hi! Cuurent time is {now}'.format(now=now))



def hi(request):
    numbers = request.GET.get('numbers', '')   
    numbers_list = [int(num) for num in numbers.split(',')] 
    sorted_numbers = sorted(numbers_list)  
    
    response_data = {
        'sorted_numbers': sorted_numbers
    }
    
    return JsonResponse(response_data)

def sayhi(request, name, age):
    if age < 12:
        message = 'sorry {} you are allowed here'.format(name)
    else:
       message = 'Hello {} welcome'.format(name)
    return HttpResponse(message)    