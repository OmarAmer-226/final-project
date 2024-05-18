from django.contrib import admin
from book_table.models import Book_Table

# Register your models here.
class Book_TableAdmin(admin.ModelAdmin):
    list_display = ('name', 'date','time','person')

admin.site.register(Book_Table, Book_TableAdmin)