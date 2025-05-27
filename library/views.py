# library/views.py
from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import HttpResponseNotFound
from library.services import book_service
from library.exceptions import BookNotFound, BookHasNoBorrowHistory

def book_list(request):
    books = Book.objects.all()   # 여기에 동작 코드를 작성하세요 (1점)
    return render(request, 'library/book_list.html', {'books': books})


def book_history(request, book_id):
    try:
        book = book_service.get_book_by_id(book_id)
        histories = book_service.get_borrow_history_for_book(book)
    except BookNotFound as e:  # 여기에 동작 코드를 작성하세요 (1점)
        return HttpResponseNotFound(str(e))
    except BookHasNoBorrowHistory as e:  # 여기에 동작 코드를 작성하세요 (1점)
        return render(request, 'library/no_history.html', {'message': str(e)})

    return render(request, 'library/book_history.html', {
        'book': book,
        'histories': histories,
    })
