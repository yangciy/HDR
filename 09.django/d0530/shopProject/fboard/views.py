from datetime import datetime
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from fboard.models import Fboard,Comment
from member.models import Member
from django.db.models import F,Q
from django.core.paginator import Paginator
from django.core import serializers
import requests
def fList(request,nowpage,category,searchword):
    if request.method =="POST":
        category = request.POST.get('category')
        searchword = request.POST.get('searchword')
        
    if category=='first':
        qs=Fboard.objects.order_by('-f_group','f_step')

    elif category== 'title':
        qs = Fboard.objects.filter(f_title__contains=searchword)
        
    elif category== 'content':
        qs = Fboard.objects.filter(f_content__contains=searchword)
    else:
        # qs = Fboard.objects.filter(f_title__contains=searchword,f_content__contains=searchword)
        qs = Fboard.objects.filter(Q(f_title__contains=searchword)|Q(f_content__contains=searchword))
    paginator=Paginator(qs,10)
    fList = paginator.get_page(nowpage)
    
    context={'fList':fList,'nowpage':nowpage,'category':category,'searchword':searchword,'count':qs.count}
    return render(request,'fList.html',context)


def fWrite(request,nowpage,category,searchword):
    if request.method=="GET":
        return render(request,'fWrite.html',{"nowpage":nowpage,'category':category,'searchword':searchword})
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
        return redirect('fboard:fList',nowpage,category,searchword)

def fView(request,f_no,nowpage,category,searchword):
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
    context={'board':qs,'boardPrev':qsPrev,'boardNext':qsNext,'nowpage':nowpage,'category':category,'searchword':searchword}
    return render(request,'fView.html',context)

def fDelete(request,f_no,nowpage,category,searchword):
    qs = Fboard.objects.get(f_no=f_no)
    qs.delete()
    return redirect('fboard:fList',nowpage,category,searchword)

def fUpdate(request,f_no,nowpage,category,searchword):
    if request.method=="GET":
        qs =Fboard.objects.get(f_no=f_no)        
        context = {'board':qs,'nowpage':nowpage,'category':category,'searchword':searchword}
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
        return redirect('fboard:fList',nowpage,category,searchword)


def fReply(request,f_no,nowpage):
    if request.method=='GET':
        qs= Fboard.objects.get(f_no=f_no)
        category='first'
        searchword='first'
        context={'board':qs,'nowpage':nowpage,'category':category,'searchword':searchword}
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

        return redirect('fboard:fList',nowpage,category,searchword)
    
    
def public_list(request):
    m_serviceKey ='735273586a64696436366a42455765'
    page=request.GET.get('page')
    if not page:
        page=1
    url='http://openapi.seoul.go.kr:8088/{}/json/VwsmTrdarSelngQq/{}/11/'.format(m_serviceKey,page)
    res= requests.get(url)
    json_res= json.loads(res.text)
    dList = json_res['VwsmTrdarSelngQq']['row']
    print(dList)
    # body= json_res['VwsmSignguIxQq']['row']
    # print(body)
    context={"dList":dList}
    return render(request,'public_list.html',context)

# list타입 queryset

def commList(request):
    f_no = request.GET.get('f_no')
    print("f_no commList : ",f_no)
    # f_no 하단댓글을 검색
    qs = Comment.objects.filter(fboard=f_no).order_by('-c_no')
    # list타입으로 전송 : safe=False
    clist = list(qs.values()) # [0:q1,1:q2,2:q3]
    return JsonResponse(clist,safe=False) 

    # HttpResponse : json타입 - dic타입
    # clist = serializers.serialize('json',qs)
    # return HttpResponse(clist,content_type='text/json-comment-filtered')
    
    # JsonResponse : dic타입으로 전송
    # context={"clist":clist}
    # # context={'reload_all':False,"clist":clist}
    # return JsonResponse(context) 
# write query
def commWrite(request):
    # html페이지에서 데이터 가져오기
    id = request.session.get('session_id')
    member = Member.objects.get(id=id)
    f_no = request.GET.get('f_no')
    fboard = Fboard.objects.get(f_no=f_no)
    pw = request.GET.get('pw')
    content = request.GET.get('content')
    # db에 저장
    qs = Comment(member=member,fboard=fboard,c_pw=pw,c_content=content)
    qs.save()
    # 댓글번호 넘겨줌
    c_no = qs.c_no
    c_date = qs.c_date
    # 저장데이터 : c_no,member,fboard,c_pw,c_content,c_date
    context={"c_no":c_no,"f_no":f_no,"c_pw":pw,"c_content":content,"c_date":c_date}
    return JsonResponse(context)

# 이벤트
def event(request):
    return render(request,'event.html')

# 이벤트 뷰
def event_view(request):
    print("f_no : ",request.GET.get('f_no'))
    # GET으로 받은 f_no를 넘겨줌.
    context={'f_no':request.GET.get('f_no')}
    return render(request,'event_view.html',context)

def commUpdateOk(request):
    c_no = request.GET.get('c_no')
    c_content = request.GET.get('c_content')
    id = request.session.get('session_id')
    print("commUpdateOk : ",c_no,c_content,id)
    # 해당데이터 검색
    qs = Comment.objects.get(c_no=c_no)
    qs.c_content = c_content
    qs.c_date=datetime.now()
    qs.save()
    # ajax으로 전송
    context={'c_no':c_no,'c_content':c_content,'c_date':qs.c_date,'result':'댓글이 수정되었습니다.'}
    return JsonResponse(context)

def commDelete(request):
    c_no = request.GET.get('c_no')
    qs = Comment.objects.get(c_no=c_no)
    qs.delete()
    context={'result':'댓글이 삭제되었습니다.'}
    return JsonResponse(context)