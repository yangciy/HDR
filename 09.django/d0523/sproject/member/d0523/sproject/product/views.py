from django.shortcuts import render,redirect
from product.models import Product
from member.models import Member


#상품 등록 함수
def pWrite(request):
    if request.method=='GET':
        return render(request,'pWrite.html')
    else:
        bName=request.POST.get('name')
        bServing=request.POST.get('serving')
        bUnitPrice=request.POST.get('price')
        bDescription=request.POST.get('content')
        bCategory=request.POST.get('cate')
        bManufacturer=request.POST.get('manufac')
        bUnit=request.POST.get('pcount')
        bFileName=request.FILES.get('file',None) #form 에서 파일 받아오는 방법
        
        Product.objects.create(pName=bName,pServing=bServing,pUnitPrice=bUnitPrice,pDescription=bDescription,pCategory=bCategory,pManufacturer=bManufacturer,pUnit=bUnit,pFileName=bFileName)
       
        return redirect('product:pList')

def pList(request):
    qs=Product.objects.order_by('pNo')
    context={'pList':qs}
    
    return render(request,'pList.html',context)