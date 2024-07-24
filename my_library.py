import json
import os

LIBRARY_FILE = 'my_library.json'


class Book:

    def __init__(
            self, id: int, title: str, author: str, year: str, status: str
    ) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status,
        }


def load_library() -> list:
    if not os.path.exists(LIBRARY_FILE):
        return []
    with open(LIBRARY_FILE, 'r') as file:
        return [Book(**book) for book in json.load(file)]


def save_library(library: list[Book]) -> None:
    with open(LIBRARY_FILE, 'w') as file:
        json.dump([book.to_dict() for book in library], file)


def add_book(library: list[Book], title: str, author: str, year: str) -> None:
    id = max([book.id for book in library], default=0) + 1
    new_book = Book(id, title, author, year, status='в наличии')
    library.append(new_book)
    save_library(library)
    print('Книга сохранена')


def remove_book(library: list[Book], id: int) -> None:
    book = [book for book in library if book.id == id]
    if book:
        library.remove(*book)
        save_library(library)
        print('Книга удалена')
    else:
        not_found_book()


def search_book(library: list[Book], query: str) -> None:
    results = [
        book for book in library if query in (
            book.title, book.author, book.year
        )
    ]
    if results:
        repr_results(results)
    else:
        not_found_book()


def get_all_books(library: list[Book]) -> None:
    results = [book for book in library]
    if results:
        repr_results(results)
    else:
        print('В библиотеке пока нет книг')


def change_status(library: list[Book], id: int, new_status: str) -> None:
    book = [book for book in library if book.id == id]
    if book and new_status in ('в наличии', 'выдана'):
        book[0].status = new_status
        save_library(library)
        print('Статус книги изменён')
    elif new_status not in ('в наличии', 'выдана'):
        print('-> Введён неверный статус')
    else:
        not_found_book()


def not_found_book() -> None:
    print('-> Книга не найдена')


def repr_results(results: list[Book]) -> None:
    for book in results:
        print(
            f'ID: {book.id}, '
            f'Название: {book.title}, '
            f'Автор: {book.author}, '
            f'Год: {book.year}, '
            f'Статус: {book.status}'
        )


def main() -> None:
    library = load_library()
    while True:
        print(
            '1. Добавить книгу\n'
            '2. Удалить книгу\n'
            '3. Найти книгу\n'
            '4. Показать все книги\n'
            '5. Изменить статус книги\n'
            '6. Выход\n'
        )
        choice = input('Выберите действие: ')

        if choice == '1':
            title = input('Введите название книги: ')
            author = input('Введите имя автора: ')
            year = input('Введите год издания: ')
            add_book(library, title, author, year)

        elif choice == '2':
            id = int(input('Введите ID книги, которую нужно удалить: '))
            remove_book(library, id)

        elif choice == '3':
            query = input(
                'Введите название, автора или год издания для поиска: '
            )
            search_book(library, query)

        elif choice == '4':
            get_all_books(library)

        elif choice == '5':
            id = int(input('Введите ID книги: '))
            new_status = input(
                'Введите новый статус книги (в наличии/выдана): '
            )
            change_status(library, id, new_status)

        elif choice == '6':
            break

        else:
            print('-> Неверный выбор, попробуйте снова.')

        print('_' * 50)


if __name__ == '__main__':
    main()
