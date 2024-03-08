from src import my_lib
import pytest


# Тест функций для поиска чисел фибоначи
class TestFibonacci:

    # Тестируем программу на корректных данных. Функция возвращает список элементов
    def test_on_correct_n(self):
        assert my_lib.fibonacci_numbers(6) == [0, 1, 1, 2, 3, 5]

    # Тестируем программу на некорректных данных. Функция вызывает исключение TypeError
    def test_with_char(self):
        with pytest.raises(TypeError):
            my_lib.fibonacci_numbers("a")
