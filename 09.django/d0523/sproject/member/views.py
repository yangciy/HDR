from django.shortcuts import redirect, render
from member.models import Member
def login(request):
    if request.method == 'GET':    
        return render(request,'login.html')
    else:
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        try:
            # id, pw가 존재할 시
            qs=Member.objects.get(id=id,pw=pw)
            request.session['session_id']= qs.id
            request.session['session_nickname']= qs.nickname
            # 메인화면으로
            # return render(request,'index.html') # 상단 url주소가 변경되지 않음.
            return redirect('/')

        except Member.DoesNotExist:
            qs= None
            # id,pw가 존재하지 않을 시
            msg='아이디 또는 비밀번호가 일치하지 않습니다.\\n다시 입력해주세요.'
            return render(request,'login.html',{'msg':msg})
        # if qs:
        #     request.session['session_id']= qs.id
        #     request.session['session_nickname']= qs.nickname
        #     # 메인화면으로
        #     # return render(request,'index.html') # 상단 url주소가 변경되지 않음.
        #     return redirect('/')
        # else :
        #     msg='아이디 또는 비밀번호가 일치하지 않습니다. 다시 입력해주세요.'
        #     return render(request,'login.html',{'msg':msg})
        

def logout(request):
    request.session.clear()
    return redirect('/')
    
