from django.shortcuts import redirect, render
from fboard.models import Fboard
from member.models import Member
from django.db.models import F
from django.core.paginator import Paginator

def fList(request,nowpage):
    qs=Fboard.objects.order_by('-f_group','f_step')
    paginator=Paginator(qs,10)
    fList = paginator.get_page(nowpage)
    context={'fList':fList,'nowpage':nowpage}
    return render(request,'fList.html',context)

def fWrite(request,nowpage):
    if request.method=="GET":
        return render(request,'fWrite.html',{"nowpage":nowpage})
    else:
        id= request.POST.get('id')
        member= Member.objects.get(id=id)
        title= request.POST.get('title')
        content= request.POST.get('content')
        file = request.FILES.get('file',None)

        qs=Fboard(member=member,f_title=title,f_content=content,f_file=file)
        qs.save()
        qs.f_group= qs.f_no
        qs.save()
        return redirect('fboard:fList',nowpage)

def fView(request,f_no,nowpage):
    qs= Fboard.objects.get(f_no=f_no)
    try:
        qs_prev=Fboard.objects.filter(f_group=qs.f_group,f_step__lt=qs.f_step).order_by('-f_group','f_step').last().f_no
    except:    
        try:
            qs_prev=Fboard.objects.filter(f_group__gt=qs.f_group).order_by('-f_group','f_step').last().f_no
        except:
            # 마지막 게시글 선택시 에러 방지
            qs_prev=Fboard.objects.order_by('-f_group','f_step').first().f_no
            
    qsPrev = Fboard.objects.get(f_no=qs_prev)
    try:
        qs_next=Fboard.objects.filter(f_group=qs.f_group,f_step__gt=qs.f_step).order_by('-f_group','f_step').first().f_no
    except:    
        try:
            qs_next=Fboard.objects.filter(f_group__lt=qs.f_group).order_by('-f_group','f_step').first().f_no
        except:
            # 마지막 게시글 선택시 에러 방지
            qs_next=Fboard.objects.order_by('-f_group','f_step').last().f_no
            
    qsNext = Fboard.objects.get(f_no=qs_next)
    qs.f_hit+=1
    qs.save()
    context={'board':qs,'boardPrev':qsPrev,'boardNext':qsNext,'nowpage':nowpage}
    return render(request,'fView.html',context)

def fDelete(request,f_no,nowpage):
    qs = Fboard.objects.get(f_no=f_no)
    qs.delete()
    return redirect('fboard:fList',nowpage)

def fUpdate(request,f_no,nowpage):
    if request.method=="GET":
        qs =Fboard.objects.get(f_no=f_no)
        context = {'board':qs,'nowpage':nowpage}
        return render(request,'fUpdate.html',context)
    else:

        id = request.POST.get('id')
        title= request.POST.get('title')
        content= request.POST.get('content')
        file = request.FILES.get('file',None)
        

        qs =Fboard.objects.get(f_no=f_no)
        qs.f_title= title
        qs.f_content= content
        if file:
            qs.f_file = file
        qs.save()
        return redirect('fboard:fList',nowpage)


def fReply(request,f_no,nowpage):
    if request.method=='GET':
        qs= Fboard.objects.get(f_no=f_no)
        context={'board':qs,'nowpage':nowpage}
        return render(request,'fReply.html', context)
    else:
        id= request.POST.get('id')
        member = Member.objects.get(id=id)
        title = request.POST.get('title')
        content = request.POST.get('content')
        group = int(request.POST.get('group'))
        step = int(request.POST.get('step'))
        indent = int(request.POST.get('indent'))
        
        file = request.FILES.get('file',None)
        reboard=Fboard.objects.filter(f_group=group, f_step__gt=step)
        reboard.update(f_step=F('f_step')+1)
        qs=Fboard(member=member,f_title=title,f_content=content,f_group=group,f_step=step+1,f_indent=indent+1,f_file=file)
        qs.save()
        
        return redirect('fboard:fList',nowpage)
    