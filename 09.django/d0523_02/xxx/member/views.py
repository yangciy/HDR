from django.shortcuts import redirect, render
from member.models import Member

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        try:
            qs=Member.objects.get(id=id,pw=pw)
            request.session['session_id']=qs.id
            request.session['session_nickname']=qs.nickname
            
            return redirect('/')
        except Member.DoesNotExist:
            qs=None
            msg='아이디 또는 비밀번호가 일치하지 않습니다. 다시 입력해주세요'
            return render(request,'login.html',{'msg':msg})
        
        
def logout(request):
    request.session.clear()
    return redirect('/')