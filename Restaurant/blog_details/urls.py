from django.urls import path
from blog_details import views

urlpatterns = [
    path('', views.blog_details, name='blog_details')
]
