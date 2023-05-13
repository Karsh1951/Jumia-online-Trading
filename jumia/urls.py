
from django.contrib import admin
from django.urls import path

from base.views import index, contact

urlpatterns = [
    #path sshould be empty because its the front page
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('admin/', admin.site.urls),
]
