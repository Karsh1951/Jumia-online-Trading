from django.contrib import admin
#.models is used because it is in the same folder as admin.py(item)
from .models import Category, Item
#registering the categories
admin.site.register(Category)
admin.site.register(Item)
#git remote add origin https://github.com/Karsh1951/Jumia-online-Trading.git
# Register your models here.
