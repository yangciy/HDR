from django.shortcuts import redirect, render
from product.models import Product
from django.core.paginator import Paginator

def pList(request, nowpage):
    qs= Product.objects.order_by('-p_no')
    paginator= Paginator(qs,10)         # 1페이지당 게시글 10개
    pList = paginator.get_page(nowpage)    # 요청한 페이지의 게시글을 전달
    context={'pList':pList,'nowpage':nowpage}
    return render(request,'pList.html',context)

def pWrite(request, nowpage):
    if request.method=="GET":
        return render(request,'pWrite.html',{'nowpage':nowpage})
    else :
        name= request.POST.get('name')
        servings= request.POST.get('servings')
        price= request.POST.get('price')
        description= request.POST.get('description')
        category= request.POST.get('category')
        manufacturer= request.POST.get('manufacturer')
        hno=request.POST.get('hno')
        file = request.FILES.get('file',None)
        

        qs=Product(p_name=name,p_hno=hno,p_servings=servings,p_unitPrice=price,p_description=description,p_category=category,p_manufacturer=manufacturer,p_filename=file)
        qs.save()
        return redirect('product:pList', nowpage)        