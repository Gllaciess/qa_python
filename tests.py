from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollectornano 
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()nan


    def test_set_book_genre_valid_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'




    def test_get_book_genre_returns_correct_genre(self):
        collector = BooksCollector()


        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'




    def test_get_books_with_specific_genre_no_books_returns_empty_list(self):
        collector = BooksCollector()


        books = collector.get_books_with_specific_genre('Фантастика')
        assert books == []




    def test_get_books_genre_returns_correct_books(self):
        collector = BooksCollector()
      

        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert 'Гарри Поттер' in collector.get_books_genre()
      


    def test_get_books_for_children_excludes_age_rating_genres(self):
        collector = BooksCollector()


        collector.add_new_book('Добрая книга')
        collector.add_new_book('Страшная книга')
        collector.set_book_genre('Добрая книга', 'Комедии')
        collector.set_book_genre('Страшная книга', 'Ужасы')
        children_books = collector.get_books_for_children()
        assert 'Добрая книга' in children_books



    def test_get_books_for_children_empty_returns_empty_list(self):
        collector = BooksCollector()

        assert collector.get_books_for_children() == []


    def test_add_book_in_favorites_positive(self):
        collector = BooksCollector()


        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        assert 'Гарри Поттер' in collector.get_list_of_favorites_books()



    def test_add_book_in_favorites_book_not_in_books_genre_not_added(self):
        collector = BooksCollector()


        collector.add_book_in_favorites('Несуществующая книга')
        assert 'Несуществующая книга' not in collector.get_list_of_favorites_books()




    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()


        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.delete_book_from_favorites('Гарри Поттер')
        assert 'Гарри Поттер' not in collector.get_list_of_favorites_books()




    def test_get_list_of_favorites_books_returns_correct_list(self):
        collector = BooksCollector()


        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Властелин колец')
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 2
        assert 'Гарри Поттер' in favorites
        assert 'Властелин колец' in favorites




