import unittest
from booklover import BookLover


class BookLoverTestSuite(unittest.TestCase):
    """Unit tests for BookLover class. Inherits from the unittest.TestCase class
    """

    def test_1_add_book(self):
        """Tests adding a book to BookLover.book_list via the add_book method. Passes if the book is added.
        """
        test_object = BookLover(
            "Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_title = 'War of the Worlds'
        test_object.add_book(book_title, 4)
        self.assertTrue(book_title, f'{book_title} is not in the book list!')

    def test_2_add_book(self):
        """Tests adding a duplicate bok to BookLover.book_list via the add_book method. Passes if the duplicate book is not added.
        """
        test_object = BookLover(
            "Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_title = 'War of the Worlds'
        try:
            test_object.add_book(book_title, 4)
            test_object.add_book(book_title, 3)
        except IndexError:
            self.assertEqual(len(test_object.book_list), 1, f'{book_title} is in the book list more than once!')

    def test_3_has_read(self):
        """Tests the BookLover.has_read method for a book in BookLover.book_list. Passes if has_read returns True.
        """
        test_object = BookLover(
            "Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_title = 'War of the Worlds'
        test_object.add_book(book_title, 4)
        self.assertTrue(test_object.has_read(book_title), f'{book_title} is not in the book list!')

    def test_4_has_read(self):
        """Tests the BookLover.has_read method for a book not in the BookLover.book_list. Passes if has_read returns False.
        """
        test_object = BookLover(
            "Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_title = 'War of the Worlds'
        test_object.add_book(book_title, 4)
        self.assertFalse(test_object.has_read("Butter"), 'Butter is in the book list!')

    def test_5_num_books_read(self):
        """Tests the BookLover.num_books_read method. Passes if num_books_read returns the number of books added to the book_list. 
        """
        test_object = BookLover(
            "Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book('War of the Worlds', 4)
        test_object.add_book('Cheese', 1)
        test_object.add_book('Python for Dummies', 5)
        num_read = 3
        self.assertEqual(test_object.num_books_read(), num_read, f'The number of books read is inconsistent! Expected: {num_read}, Found: {test_object.num_books_read()}')

    def test_6_fav_books(self):
        """Tests the BookLover.fav_books method. Passes if fav_books returns the number of favorite books in the book_list.
        """
        test_object = BookLover(
            "Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book('War of the Worlds', 4)
        test_object.add_book('Cheese', 1)
        test_object.add_book('Python for Dummies', 5)
        fav_books = 2
        self.assertEqual(len(test_object.fav_books()), fav_books, f'The number of favorite books is inconsistent! Expected: {fav_books}. Found: {test_object.fav_books()}')


if __name__ == '__main__':
    unittest.main(verbosity=3)
