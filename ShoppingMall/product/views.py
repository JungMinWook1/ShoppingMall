from django.shortcuts import render
from .models import Product

# Create your views here.
def bag(request):
    return render(request, 'bag.html')
