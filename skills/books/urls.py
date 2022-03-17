from operator import mod
from django.urls import path
from books.views import views
from books.views.modelview import AuthorViewSet, BookViewSet

urlpatterns = [
    path('books/', views.RetrieveBooks.as_view()),
    path('books/create/',views.CreateBook.as_view()),
    path('books/<int:book_id>', views.RetriveBookAPIView.as_view()),
    
    path('authors/', views.RetrieveAuthors.as_view()),
    path('authors/create/',views.CreateAuthor.as_view()),
    path('authors/<int:author_id>/', views.RetrieveAuthorAPIView.as_view()),
    
    path('viewset/authors/', AuthorViewSet.as_view({'get':'list'})),
    path('viewset/authors/create/', AuthorViewSet.as_view({'post':'create'})),
    path('viewset/authors/<int:author_id>/', AuthorViewSet.as_view(
        {
            'get':'retrieve',
            'put':'partial_update',
            'delete':'destroy'
        }
    )),
    
    path('viewset/books/', BookViewSet.as_view({'get':'list'})),
    path('viewset/books/create/', BookViewSet.as_view({'post':'create'})),
    path('viewset/books/<int:author_id>/', BookViewSet.as_view(
        {
            'get':'retrieve',
            'put':'partial_update',
            'delete':'destroy'
        }
    )),
    
]