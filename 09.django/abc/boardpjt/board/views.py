from django.shortcuts import render

def boardlist(request):
    return render(request,'boardList.html')