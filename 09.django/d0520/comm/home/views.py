from django.shortcuts import redirect, render

def index(request):
    if request.method=='GET':
        return render(request,'index.html')
    else:
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        return redirect('/')