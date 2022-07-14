from django.shortcuts import redirect, render
from fboard.models import Fboard
from member.models import Member
from django.db.models import F
from django.core.paginator import Paginator

def fList(request, nowpage):
    qs= Fboard.objects.order_by('-f_group','f_step')
    # page = int(request.GET.get('nowpage',1)) # page변수 전달, 없으면 1
    paginator= Paginator(qs,10)         # 1페이지당 게시글 10개
    fList = paginator.get_page(nowpage)    # 요청한 페이지의 게시글을 전달
    context={'fList':fList,'nowpage':nowpage}
    return render(request,'fList.html', context)


def fWrite(request, nowpage):
    if request.method=="GET":
        context={"nowpage":nowpage}        
        return render(request,'fWrite.html', context)
    else:
        # form넘어온 데이터
        id = request.POST.get('id')
        member=Member.objects.get(id=id)
        title = request.POST.get('title')
        content = request.POST.get('content')
        file = request.FILES.get('file',None)
        # db저장
        qs=Fboard(member=member,f_title=title,f_content=content,f_file=file)
        qs.save()
        qs.f_group= qs.f_no
        qs.save()
        return redirect('fboard:fList',nowpage)
        
        
def fView(request,f_no, nowpage):
    qs= Fboard.objects.get(f_no=f_no)
    
    # 이전글 중에 답글이 있는 것
    try:
        qs_prev=Fboard.objects.filter(f_group=qs.f_group,f_step__lt=qs.f_step).order_by('-f_gruop','f_step').last().f_no
    except:    
        try:
            qs_prev=Fboard.objects.filter(f_group__gt=qs.f_group).order_by('-f_gruop','f_step').last().f_no
        except:
            # 마지막 게시글 선택시 에러 방지
            qs_prev=Fboard.objects.order_by('-f_gruop','f_step').first().f_no
            
    qsPrev = Fboard.objects.get(f_no=qs_prev)

    qs.f_hit+=1
    qs.save()
    context={'board':qs,'boardPrev':qsPrev, 'nowpage':nowpage}
    return render(request,'fView.html',context)


def fReply(request,f_no,nowpage):
    if request.method =='GET':
        qs = Fboard.objects.get(f_no=f_no)
        context={'board':qs, 'nowpage':nowpage}
        return render(request,'fReply.html',context)
    else:
        id = request.POST.get('id')
        member = Member.objects.get(id=id)
        title = request.POST.get('title')
        content = request.POST.get('content')
        group = int(request.POST.get('group'))
        step = int(request.POST.get('step'))
        indent = int(request.POST.get('indent'))
        
        file = request.FILES.get('file',None)
        # 부모 group에서 부모보다 큰 step 1씩 증가
        reboard=Fboard.objects.filter(f_group=group, f_step__gt=step)
        # F참조객체 : db에서 검색을 해서 가져올 수 있음
        reboard.update(f_step=F('f_step')+1)
        
        # Fboard.objects.filter(f_group=group, f_step__gt=step).update(f_step=F('f_step')+1)
        
        # step: 출력순서, indent: 들여쓰기
        qs=Fboard(member=member,f_title=title,f_content=content,f_group=group,f_step=step+1,f_indent=indent+1,f_file=file)
        qs.save()
        
        return redirect('fboard:fList',nowpage)
    
    
    
def fDelete(request,f_no,nowpage):
    qs = Fboard.objects.get(f_no=f_no)
    qs.delete()
    return redirect('fboard:fList',nowpage)


def fUpdate(request,f_no,nowpage):
    if request.method=="GET":
        qs =Fboard.objects.get(f_no=f_no)
        context = {'board':qs, 'nowpage':nowpage}
        return render(request,'fUpdate.html',context)
    else:
        # 수정 form에서 데이터 전달
        id = request.POST.get('id')
        title= request.POST.get('title')
        content= request.POST.get('content')
        # 기존 홀란드.jpg
        # 파일을 새롭게 등록하지 않으면 None이 들어감
        file = request.FILES.get('file',None)
        
        
        # db에 수정저장
        qs =Fboard.objects.get(f_no=f_no)
        qs.f_title= title
        qs.f_content= content
        if file:
            qs.f_file = file

            
        qs.save()
        return redirect('fboard:fList',nowpage)
    

    