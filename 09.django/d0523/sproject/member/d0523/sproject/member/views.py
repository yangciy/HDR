from django.shortcuts import redirect, render
from member.models import Member

#로그인함수
def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        lId=request.POST.get('id')
        lPw=request.POST.get('pw')
        
        try:
            qs=Member.objects.get(mId=lId,mPw=lPw)
            request.session['memberID']=qs.mId
            request.session['memberNick']=qs.mNickname
            return redirect('/')
        except Member.DoesNotExist:
            msg='아이디 또는 비밀번호가 일치하지 않습니다. \\n다시 로그인 해주세요.'
            return render(request,'login.html',{'msg':msg})
        
#로그아웃함수        
def logout(request):
    request.session.clear()
    return redirect('/')