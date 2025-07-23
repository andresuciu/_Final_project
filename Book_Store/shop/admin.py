from django.contrib import admin
from .models import Book, Author, Category, Status

# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Category)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status_name')

