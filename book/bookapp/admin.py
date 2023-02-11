from django.contrib import admin
from bookapp.models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display=['title']


admin.site.register(Book,BookAdmin)