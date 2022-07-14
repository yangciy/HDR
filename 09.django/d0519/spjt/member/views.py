from django.shortcuts import redirect, render
from member.models import Member


def login(request):
    if request.method=='GET':
        print('login get 호출: login.html')
        return render (request,'login.html')      
    else:
        print('login post 호출: loginOk')
        id= request.POST.get('m_id')
        pw= request.POST.get('m_pw')
        # qs 없을 때 error
        try:
            qs = Member.objects.get(m_id=id,m_pw=pw)
        except Member.DoesNotExist:
            qs = None
            
        if qs:
            # 아이디와 패스워드 확인 로그인 가능
            # {} 입력방법 {"memberList":qs}
            # context[memberList] = qs        
            request.session['session_id']=qs.m_id
            request.session['session_name']=qs.m_name
            request.session['msg']='로그인 성공'
            return redirect('/',message='로그인 성공')
        else:
            msg='아이디 또는 패스워드가 일치하지 않습니다. 다시 로그인 하세요.'
            return render(request,'login.html',{'message':msg})
        # 세션추가

def logout(request):
    # session 모두삭제
    request.session.clear()
    # 한개의 세션 삭제
    # del request.session['session_id']
    return redirect('/')

        
def list(request):
    qs= Member.objects.order_by('-m_no')
    context={'memberList':qs}
    return render (request,'list.html',context)
# Create your views here.
