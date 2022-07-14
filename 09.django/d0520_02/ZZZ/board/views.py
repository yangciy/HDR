from django.shortcuts import render
from board.models import Board
def list(request):
    qs= Board.objects.order_by('-Z_no')
    context = {'List':qs}
    return render(request,'list.html',context)
