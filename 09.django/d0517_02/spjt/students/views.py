from django.shortcuts import render
from students.models import Student
def register(request):
    # qs2 = Student(s_name='이순신',s_major='군사학과',s_age=24)
    # qs2.save()
    
    # qs3 = Student(s_name='유관순',s_major='영문학과',s_age=10)
    # qs3.save()
    # qs4 = Student(s_name='강감찬',s_major='역사학과',s_age=20)
    # qs4.save()
    # qs5 = Student(s_name='김구',s_major='법학과',s_age=23)
    # qs5.save()
    
    qs=Student.objects.get(s_name='강감찬')
    qs.delete()
    
    
    
    
    qs=Student.objects.all()
    print(qs)
    return render(request,'register.html')