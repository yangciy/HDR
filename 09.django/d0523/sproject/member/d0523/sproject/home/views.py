from django.shortcuts import render
from product.models import Product

def index(request):
    qs=Product.objects.order_by('pNo')[:3]
    return render(request,'index.html',{'pItems':qs})