from django.shortcuts import redirect, render
from fboard.models import Fboard
from member.models import Member
def fList(request):
    qs= Fboard.objects.order_by('-f_group','f_step')
    context={'fList':qs}
    return render(request,'fList.html', context)


def fWrite(request):
    if request.method=="GET":
        return render(request,'fWrite.html')
    else:
        id = request.POST.get('id')
        member=Member.objects.get(id=id)
        title = request.POST.get('title')
        content = request.POST.get('content')
        file = request.POST.get('file',None)
        
        qs= Fboard(member=member,f_title=title,f_content=content,f_file=file)
        qs.save()
        qs.f_group=qs.f_no
        qs.save()
        return redirect('fboard:fList')
    

def fView(request,f_no):
    qs= Fboard.objects.get(f_no=f_no)
    context={'board':qs}
    return render(request,'fView.html',context)

def fReply(request,f_no):
    if request.method == "GET":
        qs= Fboard.objects.get(f_no=f_no)
        context={'board':qs}
        return render(request,'fReply.html',context)
    else:
        id = request.POST.get('id')
        member =Member.objects.get(id=id)
        title = request.POST.get('title')
        content = request.POST.get('content')
        gruop = int(request.POST.get('group'))
        step = int(request.POST.get('step'))
        indent = int(request.POST.get('indent'))