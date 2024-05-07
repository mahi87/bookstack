from rest_framework import serializers

from books.models.book import Book


class BookForm(serializers.Serializer):
    title = serializers.CharField()
    author = serializers.CharField()
    publication_year = serializers.IntegerField()
    genre = serializers.CharField()

    def create(self, validated_data):
        book = Book.objects.create(**validated_data)
        return book
