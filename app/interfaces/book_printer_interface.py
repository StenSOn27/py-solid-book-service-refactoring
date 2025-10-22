from abc import abstractmethod

from app.interfaces.book_interface import BookInterface


class BookPrinterInterface(BookInterface):
    @abstractmethod
    def print_book(self, print_type: str) -> None:
        pass
