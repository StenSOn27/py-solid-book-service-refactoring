from abc import abstractmethod

from app.interfaces.book_interface import BookInterface


class BookSerializerInterface(BookInterface):
    @abstractmethod
    def serialize(self, serialize_type: str) -> str:
        pass
