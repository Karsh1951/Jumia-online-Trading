
from django.shortcuts import render,redirect
#information about the browser IP address(GET or POST request)
from item.models import Category, Item
from .forms import SignupForm
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

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            form = SignupForm()
    form = SignupForm()
    
    return render (request, 'base/signup.html', {
        'form': form
    })
