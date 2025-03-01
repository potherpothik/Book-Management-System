from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='index'),  # Changed from 'book_list'
    path('create/', views.BookCreateView.as_view(), name='book_create'),
    path('update/<int:pk>/', views.BookUpdateView.as_view(), name='book_update'),
    path('delete/<int:pk>/', views.BookDeleteView.as_view(), name='book_delete'),
]