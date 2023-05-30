from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Product

# Create your views here.
def bag(request):
    pro = Product.objects.all().order_by('pk')
    return render(request, 'bag.html', {'pro':pro})
