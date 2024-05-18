from django.shortcuts import render

# Create your views here.
def blog_details(request):
    return render(request,'Blogdetails/blog_details.html')