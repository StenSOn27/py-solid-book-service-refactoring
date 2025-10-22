from abc import abstractmethod

from app.interfaces.book_interface import BookInterface


class BookDisplayInterface(BookInterface):
    @abstractmethod
    def display(self, display_type: str) -> None:
        pass
