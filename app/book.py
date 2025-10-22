from app.displayer import ConsoleBookDisplay, ReverseBookDisplay
from app.printer import ConsoleBookPrinter, ReverseBookPrinter
from app.serializer import JsonBookSerializer, XMLBookSerializer


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

        self.strategies = {
            "display": {
                "console": ConsoleBookDisplay.display,
                "reverse": ReverseBookDisplay.display,
            },
            "print": {
                "console": ConsoleBookPrinter.print_book,
                "reverse": ReverseBookPrinter.print_book,
            },
            "serialize": {
                "json": JsonBookSerializer.serialize,
                "xml": XMLBookSerializer.serialize,
            }
        }
