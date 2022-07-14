from django.shortcuts import render

# 회원전체리스트 함수
def memberList(request):
    return render(request,'memberList.html')


def login(reqeust):
    return render(reqeust,'login.html')


def list(request):
    return render(request,'list.html')