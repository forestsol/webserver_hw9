# library/urls.py

from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('books/', views.book_list, name='book_list'),  # 여기에 동작 코드를 작성하세요 (1점)
    path('books/<int:book_id>/history/', views.book_history, name='book_history'),  # 여기에 동작 코드를 작성하세요 (1점)
]
