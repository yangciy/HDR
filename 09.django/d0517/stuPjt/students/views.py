from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from students.models import Student

# 학생 등록 함수
def stuWrite(request):
    # get
    if request.method=='GET':
        return render(request,'stuWrite.html')
    # post
    else:
        name = request.POST.get('name')
        major = request.POST.get('major')
        age = request.POST.get('age')
        grade = request.POST.get('grade')
        gender = request.POST.get('gender')
        print('form name : ',name)
        # DB 저장
        Student.objects.create(s_name=name,s_major=major,s_age=age,s_grade=grade,s_gender=gender)
        # qs = Student(s_name=name,s_major=major,s_age=age,s_grade=grade,s_gender=gender)
        # qs.save()    
        return HttpResponseRedirect(reverse('index'))
   
# 학생 전체 리스트
def stuList(request):
    qs=Student.objects.order_by('s_name')
    count =qs.count()
    # dic타입으로 저장
    context = {'stuList':qs,'stuCount':count}
    # context데이터를 html에 보냄
    return render(request,'stuList.html',context)
   
# 학생 상세 페이지
def stuView(request,name):
    # name변수를 가지고 학생 검색 - 타입: Student 객체
    qs = Student.objects.get(s_name=name)
    context={'stu':qs}
    return render(request,'stuView.html', context)


# def stuView(request):
#     name= request.GET.get('name')
#     # name변수를 가지고 학생 검색 - 타입: Student 객체
#     qs = Student.objects.get(s_name=name)
#     context={'stu':qs}
#     return render(request,'stuView.html',context)
    
   
   
   
   
   
   
   
# 학생 DB 등록 - form 데이터 전달 받음 : name, major, age, grade, gender
# def stuWriteOk(request):
#     # form데이터 읽기 - post
#     name = request.POST.get('name')
#     major = request.POST.get('major')
#     age = request.POST.get('age')
#     grade = request.POST.get('grade')
#     gender = request.POST.get('gender')
#     print('form name : ',name)
#     # DB 저장
#     Student.objects.create(s_name=name,s_major=major,s_age=age,s_grade=grade,s_gender=gender)
#     # qs = Student(s_name=name,s_major=major,s_age=age,s_grade=grade,s_gender=gender)
#     # qs.save()
    

#     return HttpResponseRedirect(reverse('index'))
    
    
    
    
    
    
    
    
    ###### db명령어
    # # 1.crate
    # # query = Student(s_name='홍길순',s_major='영문학과',s_age=24, s_grade=4, s_gender='여자')
    # # query.save()
    # # db접근을 해서 정보를 가져옴.
    # # 2.read
    # qs = Student.objects.all()
    # print(qs)
    # # 3.search
    # qs2 = Student.objects.get(s_name='홍길동')
    # print(qs2)
    # qs3 = Student.objects.filter(s_name__contains='홍')
    # print(qs3)
    # # 4. update
    # qs4 = Student.objects.get(s_name='홍길동')
    # qs4.s_major= '아동학과'
    # qs4.save()
    # print('변경되었습니다.')
    # # 5. delete
    # # qs5 = Student.objects.get(s_name='홍길자')
    # # qs5.delete()
    # # print('삭제되었습니다.')