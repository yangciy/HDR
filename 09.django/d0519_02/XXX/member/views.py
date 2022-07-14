from django.shortcuts import render
from member.models import Member

def list(request):
    qs= Member.objects.order_by('-s_no')
    context={'memberList':qs}
    return render(request,'list.html',context)
