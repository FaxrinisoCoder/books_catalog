from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Book


def book_list(request):
    query = request.GET.get('q')
    favorites_only = request.GET.get('favorite')

    books = Book.objects.all().order_by('-id')

    if query:
        books = books.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(genre__icontains=query)
        )

    if favorites_only == '1':
        books = books.filter(is_favorite=True)

    context = {
        'books': books,
        'query': query,
        'favorites_only': favorites_only,
    }
    return render(request, 'books/book_list.html', context)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})