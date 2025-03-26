from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, RetrieveDestroyAPIView, \
    DestroyAPIView, ListCreateAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Book
from rest_framework import serializers, status

from .serializers import BookSerializer


# Create your views here.
#
# class BookListAPIView(ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookListAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True).data
        data= {
            "status": f"Returned {len(serializer)} books",
            "books": serializer
        }
        return Response(data)

# class BookDetailAPIView(RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book)
            data={
                "status":"Success",
                "book": serializer.data
            }
            return Response(data,status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response(
                {"status": "Error", "message": "Book not found"},
                status=status.HTTP_404_NOT_FOUND
            )




# class BookCreateAPIView(CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookCreateAPIView(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"status": "Error", "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

        book = serializer.save()
        data = {
            "status": f"Saved book: {book.title}",
            "book": serializer.data
        }
        return Response(data, status=status.HTTP_201_CREATED)


# class BookDeleteAPIView(DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
class BookDeleteAPIView(APIView):
    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()

            return Response(
                {"status": "Success"},
                status=status.HTTP_200_OK
            )
        except Book.DoesNotExist:
            return Response(
                {"status": "Error", "message": "Book not found"},
                status=status.HTTP_404_NOT_FOUND,
            )


# class BookUpdateAPIView(UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookUpdateAPIView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(),id=pk)
        data = request.data
        serializers =BookSerializer(instance=book,data=data,partial=True)
        if not serializers.is_valid():
            return Response(
                {"status": "Error", "errors": serializers.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
        book = serializers.save()
        data = {
            "status": f"Saved book: {book.title}",
            "book": serializers.data
        }
        return Response(data, status=status.HTTP_201_CREATED)

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookListCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



