from django.shortcuts import render, get_object_or_404
from .models import Item

# Create your views here.
#to find details of an item
def detail(request, pk):
    item = get_object_or_404(Item,pk=pk)
    
    return render(request, 'item/details.html',{'item': item})
