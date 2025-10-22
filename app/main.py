from app.book import Book


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        try:
            strategy = book.strategies[cmd][method_type]
            return strategy(book)
        except ValueError as er:
            print("ValueError", er)

if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
