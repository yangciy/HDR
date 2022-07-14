from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from students.models import Student

def stuWrite(request):
    return render(request,'stuWrite.html')

def stuWriteOk(request):
    name = request.POST.get('name')
    major = request.POST.get('major')
    age = request.POST.get('age')
    grade = request.POST.get('grade')
    gender = request.POST.get('gender')
    hobby = request.POST.getlist('hobby')
    hobby = ','.join(hobby)
    Student.objects.create(s_name=name,s_major=major,s_age=age,s_grade=grade,s_gender=gender,s_hobby=hobby)
    return HttpResponseRedirect(reverse('students:stuList'))

def stuList(request):
    qs= Student.objects.order_by('s_no')
    count= qs.count()
    context={'stuList':qs,'count':count}
    return render(request,'stuList.html',context)

def stuView(request, s_no):
    qs= Student.objects.get(s_no=s_no)
    context={'stu':qs}
    return render(request,'stuView.html',context)


def stuUpdate(request, s_no):
    qs= Student.objects.get(s_no=s_no)
    context= {'stu':qs}
    return render(request,'stuUpdate.html',context)

def stuUpdateOk(request):    
    s_no = request.POST.get('s_no')
    major = request.POST.get('major')
    age = request.POST.get('age')
    grade = request.POST.get('grade')
    gender = request.POST.get('gender')
    hobby = request.POST.getlist('hobby')
    hobby=','.join(hobby)   

    qs = Student.objects.get(s_no=s_no)
    qs.s_major=major
    qs.s_age=age
    qs.s_grade=grade
    qs.s_gender=gender
    qs.s_hobby=hobby
    qs.save()
    
    return HttpResponseRedirect(reverse('students:stuList'))

def stuDelete(request, s_no):
    qs= Student.objects.get(s_no=s_no)
    qs.delete()
    return HttpResponseRedirect(reverse('students:stuList'))

