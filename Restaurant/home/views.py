from django.shortcuts import render
from django.http import HttpResponse 
from book_table.models import Book_Table
from menu.models import Menu

# Create your views here.
def home(request):
    return render(request,'Home/home.html')

def about(request):
    return render(request,'About/about.html')

def menu(request):
     menu_list = Menu.objects.all()
     return render(request, 'Menu/menu.html',{'menu_list': menu_list})
   

def pages(request):
    return render(request,'Pages/pages.html')

def book_table(request):
    if request.method == 'Post': 
        name = request.Post.get('name')
        phone = request.Post.get('phone')
        date = request.Post.get('date')
        time = request.Post.get('time')
        person = request.Post.get('person')
        
        if name !='' and phone !='' and date!='' and time !='' and person !='':
            data = Book_Table(name = name , phone = phone , date = date , time = time , person = person)
            data.save()

    return render(request,'Booktable/book_table.html')

def contact(request):
    return render(request,'Contact/contact.html')

def blog_details(request):
    return render(request,'Blogdetails/blog_details.html')
