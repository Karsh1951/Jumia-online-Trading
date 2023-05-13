from django.shortcuts import render
#information about the browser IP address(GET or POST request)
def index (request):
    return render(request, 'base/index.html')
def contact(request):
    return render(request, 'base/contact.html')
