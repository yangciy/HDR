from django.shortcuts import redirect, render
from fboard.models import Fboard
from member.models import Member
from django.db.models import F #DB참조함수 라이브러리
from django.core.paginator import Paginator

#게시판리스트 함수
def fList(request,nowpage):
    qs=Fboard.objects.order_by('-fGroup','fStep')
    #페이징 처리
    #vpage 변수 전달, 없으면 디폴트 1로 설정
    # mypage=int(request.GET.get('nowpage',1))

    
    #1페이지 당 나타낼 게시글 수 설정
    mypaginator=Paginator(qs,10)
    fList=mypaginator.get_page(nowpage)#요청한 페이지의 게시글 10개를 전달
    context={'fList':fList,'nowpage':nowpage}
    return render(request,'fList.html',context)

#게시판 글쓰기 함수
def fWrite(request,nowpage):
    if request.method=='GET':
        return render(request,'fWrite.html',{'nowpage':nowpage})
    else:
        bId=request.POST.get('id')
        bmember=Member.objects.get(mId=bId)
        bTitle=request.POST.get('title')
        bContent=request.POST.get('content')
        bFile=request.FILES.get('file',None) #form 에서 파일 받아오는 방법
        qs=Fboard(fmember=bmember,fTitle=bTitle,fContent=bContent,fFile=bFile)
        qs.save()
        qs.fGroup=qs.fNo
        qs.save()
        return redirect('fboard:fList',nowpage)

#게시판 글 상세보기 함수
def fView(request,fNum,nowpage):
    qs = Fboard.objects.get(fNo=fNum)
    qs.fHit+=1
    qs.save()
    
    #게시판 리스트- 정렬
    #이전글
    try:#답글인 경우
        qs_prev=Fboard.objects.filter(fGroup=qs.fGroup,fStep__lt=qs.fStep).order_by('-fGroup','fStep').last().fNo
    except:#답글이 아닌 경우
        try:
            qs_prev=Fboard.objects.filter(fGroup__gt=qs.fGroup).order_by('-fGroup','fStep').last().fNo
        except:#마지막 게시글일 경우 그냥 마지막 게시글 번호 가져옴
            qs_prev=Fboard.objects.order_by('-fGroup','fStep').first().fNo
            
    preview1=Fboard.objects.get(fNo=qs_prev)
            
        
    #다음글
    try:#답글인 경우
        qs_next=Fboard.objects.filter(fGroup=qs.fGroup,fStep__gt=qs.fStep).order_by('-fGroup','fStep').first().fNo
    except:#답글이 아닌 경우
        try:
            qs_next=Fboard.objects.filter(fGroup__lt=qs.fGroup).order_by('-fGroup','fStep').first().fNo
        except:#첫번째 게시글일 경우 그냥 첫번째 게시글 번호 가져옴
            qs_next=Fboard.objects.order_by('-fGroup','fStep').last().fNo
            
    nextview1=Fboard.objects.get(fNo=qs_next)
    
    
    
    return render(request,'fView.html',{'board':qs,'boardPrev':preview1,'boardNext':nextview1,'nowpage':nowpage})

#답글 작성 함수
def fReply(request,fNum,nowpage):
    if request.method=='GET':
        qs=Fboard.objects.get(fNo=fNum)
        return render(request,'fReply.html',{'board':qs,'nowpage':nowpage})
    else:
        bId=request.POST.get('id')
        bmember=Member.objects.get(mId=bId)
        bGroup=int(request.POST.get('group'))
        #step:출력순서,indent:들여쓰기
        #request로 넘어온 데이터는 모두 str타입이라 형변환 필요
        bStep=int(request.POST.get('step'))+1
        bIndent=int(request.POST.get('indent'))+1
        print("AAAAAAAAAAAAIndent:",bIndent)
        bTitle=request.POST.get('title')
        bContent=request.POST.get('content')
        bFile=request.FILES.get('file',None)
        #같은 부모 그룹에 속한 하위 게시글의 step을 전부 1씩 증가
        step_qs=Fboard.objects.filter(fGroup=bGroup,fStep__gte=bStep)
        #F참조객체: DB에서 검색해서 가져올 수 있음
        step_qs.update(fStep=F('fStep')+1)
        
        
        qs=Fboard(fmember=bmember,fTitle=bTitle,fContent=bContent,fGroup=bGroup,fStep=bStep,fIndent=bIndent,fFile=bFile)
        qs.save()
        return redirect('fboard:fList',nowpage)
    
    
#게시글 삭제 함수
def fDelete(request,fNum,nowpage):
    qs=Fboard.objects.get(fNo=fNum)
    qs.delete()
    return redirect('fboard:fList',nowpage)


#게시글 수정 함수
def fUpdate(request,fNum,nowpage):
    if request.method=='GET':
        qs=Fboard.objects.get(fNo=fNum)
        return render(request,'fUpdate.html',{'board':qs,'nowpage':nowpage})
    else:
        #수정 form에서 데이터 전달
        bTitle=request.POST.get('title')
        bContent=request.POST.get('content')
        #tiger01.png 들어가있지만 file은 input에서 value 지정 못해서 get으로 가져올 수 없음
        bFile=request.FILES.get('file',None)
        
        
        qs=Fboard.objects.get(fNo=fNum)
        qs.fTitle=bTitle
        qs.fContent=bContent
        if bFile:
            qs.fFile=bFile
        qs.save()
        return redirect('fboard:fList',nowpage)
        
