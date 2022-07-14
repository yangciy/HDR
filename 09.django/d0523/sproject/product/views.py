from django.shortcuts import redirect, render
from product.models import Product


def pList(request):
    qs= Product.objects.order_by('-p_no')
    context={'pList':qs}
    return render(request,'pList.html',context)

def pWrite(request):
    if request.method=="GET":
        return render(request,'pWrite.html')
    else :
        name= request.POST.get('name')
        servings= request.POST.get('servings')
        price= request.POST.get('price')
        description= request.POST.get('description')
        category= request.POST.get('category')
        manufacturer= request.POST.get('manufacturer')
        file = request.FILES.get('file',None)

        qs=Product(p_name=name,p_servings=servings,p_unitPrice=price,p_description=description,p_category=category,p_manufacturer=manufacturer,p_filename=file)
        qs.save()
        return redirect('product:pList')        