import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from books.models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        title = data.get('title',None)
        author = data.get('author',None)
        if title.isdigit() :
            raise ValidationError(
                {
                    "status":False,
                    "message":"Kitob nomi faqat sondan iborat bo'shi mumkun emas ."
                }
            )
        if not re.match(r"^[A-Za-z' ]+$", author):
            raise ValidationError(
                {
                    "status":False,
                    "message":"Kitob Avtori son aralashmasligi kerak."
                }
            )
        if Book.objects.filter(title=title,author=author).exists():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Bu kitob oldin kiritilgan"
                }
            )
        return data
    def validate_price(self, price):
        if price <= 0 or price > 9999999999:
            raise ValidationError(
                {
                    "status": False,
                    "message": "Narx notog'ri kiritilgan"
                }
            )



