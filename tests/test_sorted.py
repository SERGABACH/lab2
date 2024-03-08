from src import  my_lib
import pytest


class TestSorted:

    # Функция возвращает данные для выполнения теста - упорядоченный от мин к макс список
    @pytest.fixture
    def ordered_example(self):
        return [1, 2, 3]

    # Функция возвращает данные для выполнения теста - неупорядоченный список
    @pytest.fixture
    def unordered_example(self):
        return [1, 3, 2]

    # Функция возвращает данные для выполнения теста - массив равных по величине значений
    @pytest.fixture
    def equal_example(self):
        return [1, 1, 1]

    # Тест функции на упорядоченных от мин к макс значениях
    def test_on_ordered(self, ordered_example):
        assert my_lib.bubble_sort(ordered_example) == [1, 2, 3]

    # Тест функции на неупорядоченных значениях
    def test_on_unordered(self, unordered_example):
        assert my_lib.bubble_sort(unordered_example) == [1, 2, 3]

    # Тест функции на равных по величине значениях
    def test_on_equal(self, equal_example):
        assert my_lib.bubble_sort(equal_example) == [1, 1, 1]
