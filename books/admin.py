from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'is_favorite')
    list_filter = ('genre', 'is_favorite')
    search_fields = ('title', 'author', 'genre')