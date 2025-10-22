from app.book import Book
from app.displayer import ConsoleBookDisplay, ReverseBookDisplay
from app.printer import ConsoleBookPrinter, ReverseBookPrinter
from app.serializer import JsonBookSerializer, XMLBookSerializer


BOOK_STRATEGIES = {
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


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        try:
            strategy = BOOK_STRATEGIES[cmd][method_type]
            return strategy(book)
        except ValueError as er:
            print("ValueError", er)

if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
