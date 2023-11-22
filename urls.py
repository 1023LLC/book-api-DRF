from django.urls import path

from .views import BookList, BookCreate, BookDetail

urlpatterns = [
    path('list/', BookList.as_view()),
    path('', BookCreate.as_view()),
    path('<str:pk>', BookDetail.as_view())
]