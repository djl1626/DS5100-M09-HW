import pandas as pd


class BookLover:
    """This class represents a booklover. A booklover consists the following:
        - name
        - email
        - favorite genre
        - number of books
        - book list
    """

    def __init__(self, name: str, email: str, fav_genre: str, num_books: int = 0, book_list: pd.DataFrame = pd.DataFrame({'book_name': [], 'book_rating': []})):
        """Initializes a BookLover object

        Args:
            name (str): name of the book lover
            email (str): email of the book lover
            fav_genre (str): favorite genre of the book lover
            num_books (int, optional): number of books for the book lover. Defaults to 0.
            book_list (_type_, optional): list of the book lover's books. Defaults to pd.DataFrame({'book_name': [], 'book_rating': []}).
        """
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list

    def add_book(self, book_name: str, rating: int):
        """Adds a book to the book lover's book list

        Args:
            book_name (str): name of the book to add
            rating (int): book lover's rating

        Raises:
            IndexError: raised if the book trying to be added is already in the book list
            ValueError: raised if the rating is less than 0 or greater than 5
        """
        if book_name in self.book_list['book_name']:
            raise IndexError(f'{book_name} is already in the book list!')
        elif rating < 0 or rating > 5:
            raise ValueError('rating must be between 0 and 5 inclusive')
        new_book = pd.DataFrame(
            {'book_name': [book_name], 'book_rating': [rating]})
        self.book_list = pd.concat(
            [self.book_list, new_book], ignore_index=True)
        self.num_books += 1

    def has_read(self, book_name: str) -> bool:
        """Returns True if the book lover had read a book and False otherwise

        Args:
            book_name (str): name of the book to check

        Returns:
            bool: True if the book_name is in the book lover's book_list and False otherwise
        """
        return book_name in self.book_list['book_name'].tolist()

    def num_books_read(self) -> int:
        """Returns the number of books for the book lover

        Returns:
            int: number of books for the book lover
        """
        return self.num_books

    def fav_books(self) -> pd.DataFrame:
        """Returns a pandas DataFrame containing the book lover's favorite books. Favorite books have a rating greater than 3.

        Returns:
            pd.DataFrame: pandas DataFrame containing the book lover's favorite books.
        """
        return self.book_list[self.book_list['book_rating'] > 3]
