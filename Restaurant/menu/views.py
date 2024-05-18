from django.shortcuts import render
from .models import Menu
# Create your views here.
def menu(request):
     menu_list = Menu.objects.all()
     return render(request, 'Menu/menu.html',{'menu_list': menu_list})
    