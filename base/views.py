
from django.shortcuts import render
#information about the browser IP address(GET or POST request)
from item.models import Category, Item
def index(request):
    #not to display products that are already sold
    
    items = Item.objects.filter(is_sold= False)[0:6]
    #TO GET ALL THE CATEGORIES
    categories = Category.objects.all()
    
    
    return render(request, 'base/index.html', {
                'categories':categories,
                'items':items,
                })
def contact(request):
    return render(request, 'base/contact.html')
