from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import BookListAPIView, BookDetailAPIView, BookCreateAPIView, BookDeleteAPIView, BookUpdateAPIView, \
    BookListCreateAPIView, BookViewSet

router = SimpleRouter()
router.register('books', BookViewSet, basename='books')
urlpatterns = [
    # path('books/', BookListCreateAPIView.as_view()),
    # path('book/', BookListAPIView.as_view()),
    # path('books/<int:pk>/',BookDetailAPIView.as_view()),
    # path('books/create/', BookCreateAPIView.as_view()),
    # path('books/<int:pk>/update/', BookUpdateAPIView.as_view()),
    # path('books/<int:pk>/delete/', BookDeleteAPIView.as_view()),

]

urlpatterns += router.urls