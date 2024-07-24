


# Cистема управления библиотекой

### Описание:
Консольное приложение для управления библиотекой книг. В приложении можно добавлять, удалять, искать и отображать книги.

Каждая книга содержит следующие поля:

1. `id` - уникальный идентификатор, генерируется автоматически
2. `title` - название книги
3. `author` - автор книги
4. `year` - год издания
5. `status` - статус книги: "в наличии", "выдана"
 
 Хранение данных реализовано в `json` формате.
 
### Для запуска
 1. Клонировать репозиторий
 2. Перейти в каталог с приложением

	 ```bash
	 cd my_library
	 ```

 3. Запустить проект

	 ```bash
	 python my_library.py
	 ```

В проекте уже есть БД для тестирования, можно использовать её (`my_library.json`).


### Основной функционал:

  1. `Добавить книгу` - пользователь вводит title, author и year, после
    чего книга добавляется в библиотеку с уникальным id и статусом “в
    наличии”.
  2. `Удалить книгу` - пользователь вводит id книги, которую нужно удалить.
  3. `Найти книгу` - пользователь может искать книги по title, author или
    year.
  4. `Показать все книги` - приложение выводит список всех книг с их id,
    title, author, year и status.
  5. `Изменить статус книги` - пользователь вводит id книги и новый статус
    ("в наличии" или "выдана").