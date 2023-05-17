from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from base.views import index, contact

urlpatterns = [
    #path sshould be empty because its the front page
    path('', index, name='index'),
    path('items/',include('items.urls')),
    path('contact/', contact, name='contact'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
