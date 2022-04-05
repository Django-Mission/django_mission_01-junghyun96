from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse


import random
# 횟수 입력받기
def lotto_count(reqeust):
    return render(reqeust, 'lotto_index.html')

def lotto_num(reqeust):
    count = reqeust.GET.get('count')
    result = []
    for i in count:
        line = []
        for i in range(0,int(count)):
            i = i + 1
            line = sorted(random.sample(range(1,46),6))
            result.append(line)
    return render(reqeust, 'lotto_result.html',{'result':result,'count':count})
