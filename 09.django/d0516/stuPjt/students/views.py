from django.shortcuts import render

# Create your views here.
# 학생등록페이지 호출
def register(request):
    return render(request,'register.html')