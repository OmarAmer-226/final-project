from django.urls import path
from book_table import views

urlpatterns = [
    path('', views.book_table, name='book_table')
]