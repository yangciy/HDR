# from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    # return HttpResponse('여기에 글자를 페이지에 리턴해줌')
    # 데이터 형태로 전달
    

