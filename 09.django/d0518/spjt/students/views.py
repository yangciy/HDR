from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from students.models import Student
def stuWrite(request):
    return render(request,'stuWrite.html')

def stuWriteOk(request):
    name =request.POST.get('name')        # 데이터가 넘어오지 않으면 none
    # name =request.POST['name']            # 데이터가 넘어오지 않으면 error
    major = request.POST.get('major')
    age = request.POST.get('age')
    grade = request.POST.get('grade')
    gender = request.POST.get('gender')
    hobby = request.POST.getlist('hobby')
    hobby=','.join(hobby)           # , 기준으로 조인    리스트로 만들려면 split
    # Db : list type으로 저장이 불가
    # s_hobby -> list type -> str타입
    # print("s_hobby: ",s_hobby)
    # print("s_hobby.join: ",s_hobby)
    # print("s_hobby.join.type: ",type(s_hobby))
    Student.objects.create(s_name=name,s_major=major,s_age=age,s_grade=grade,s_gender=gender,s_hobby=hobby)
    # qs = Student(s_name=name,s_major=major,s_age=age,s_grade=grade,s_gender=gender,s_hobby=hobby)
    # qs.save()
    return HttpResponseRedirect(reverse('students:stuList'))

def stuList(request):
    qs= Student.objects.order_by('s_no')      # order_by 정렬, -붙이면 역순, all은 순차
    count = qs.count()                          # 전체 리스트 개수
    context = {'stuList':qs,'count':count}
    return render(request,'stuList.html',context)


def stuView(request,s_no):
    qs=Student.objects.get(s_no=s_no)
    context= {'stu':qs}
    return render(request,'stuView.html',context)

def stuUpdate(request,s_no):
    qs=Student.objects.get(s_no=s_no)
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