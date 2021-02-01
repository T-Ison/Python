from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('authors',views.authors),
    path('processBook',views.processBook),
    path('processAuthor',views.processAuthor),
    path('books/<int:book_id>',views.bookDetail),
    path('authors/<int:author_id>',views.authorNotes),
    path('addAuthor_toBooks',views.addAuthor_toBooks),
    path('addBooks_toAuthor',views.addBooks_toAuthor),
]