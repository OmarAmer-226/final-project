from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about,name='about'),
    path('pages/',views.pages,name='pages'),
    path('contact/',views.contact,name='contact'),
    # path('login',views.login,name='login'),
    path('book_table/',views.book_table,name='book_table'),
    path('blog_detalis/',views.blog_details,name='blog_details'),
    
   
    # path('<int:post_id>/', views.blog_detail, name='blog_detail'),
]