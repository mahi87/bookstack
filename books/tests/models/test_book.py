from django.db.utils import IntegrityError
from django.test import TestCase

from books.models import Book


# Create your tests here.
class TestBook(TestCase):
    def test_with_valid_values(self):
        book_args = make_book()
        book = Book.objects.create(**book_args)

        self.assertIsNotNone(book)

    def test_with_incorrect_data_type(self):
        with self.assertRaises(ValueError):
            book_args = make_book(publication_year="foobar")
            Book.objects.create(**book_args)

    def test_missing_author_raises_error(self):
        with self.assertRaises(IntegrityError):
            book_args = make_book(author=None)
            Book.objects.create(**book_args)

    def test_missing_title_raises_error(self):
        with self.assertRaises(IntegrityError):
            book_args = make_book(title=None)
            Book.objects.create(**book_args)

    def test_missing_genre_raises_error(self):
        with self.assertRaises(IntegrityError):
            book_args = make_book(genre=None)
            Book.objects.create(**book_args)

    def test_missing_language_raises_error(self):
        with self.assertRaises(IntegrityError):
            book_args = make_book(language=None)
            Book.objects.create(**book_args)

    def test_allows_summary_to_be_nullable(self):
        book_args = make_book(summary=None)
        book = Book.objects.create(**book_args)

        self.assertIsNotNone(book)

    def test_allows_publication_year_to_be_nullable(self):
        book_args = make_book(publication_year=None)
        book = Book.objects.create(**book_args)

        self.assertIsNotNone(book)

    def test_allows_isbn_to_be_nullable(self):
        book_args = make_book(isbn=None)
        book = Book.objects.create(**book_args)

        self.assertIsNotNone(book)

    def test_allows_publisher_to_be_nullable(self):
        book_args = make_book(publisher=None)
        book = Book.objects.create(**book_args)

        self.assertIsNotNone(book)

    def test_allows_num_pages_to_be_nullable(self):
        book_args = make_book(num_pages=None)
        book = Book.objects.create(**book_args)

        self.assertIsNotNone(book)

    def test_does_not_allow_duplicate_title_author(self):
        book1_args = make_book()
        book1 = Book.objects.create(**book1_args)
        book2_args = make_book()
        book3_args = make_book(title="Fourth Wing")
        book4_args = make_book(author="Sarah J Maas")
        book3 = Book.objects.create(**book3_args)
        book4 = Book.objects.create(**book4_args)
        self.assertIsInstance(book3, Book)
        self.assertIsInstance(book4, Book)
        with self.assertRaisesMessage(
            IntegrityError, "duplicate key value violates unique constraint"
        ):
            Book.objects.create(**book2_args)


def make_book(**kwargs):
    default_book = {
        "title": "Iron Flame",
        "author": "Rebbeca Yaroos",
        "publication_year": 2023,
        "genre": "Fiction",
        "isbn": "7374952-1y48",
        "publisher": "test_publisher",
        "language": "English",
        "num_pages": 615,
        "summary": "it is a fantasy fiction about dragons",
    }

    return default_book | dict(kwargs)
