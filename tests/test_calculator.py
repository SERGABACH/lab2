from src import my_lib
import pytest



class TestCalc:

    # Тестируем программу на корректных данных. Функция возвращает число
    def test_plus(self):
        assert my_lib.calculator(1, 2, '+') == 3

    def test_subtraction(self):
        assert my_lib.calculator(1, 2, '-') == -1

    def test_mult(self):
        assert my_lib.calculator(1, 2, '*') == 2

    def test_div(self):
        assert my_lib.calculator(1, 2, '/') == 0.5

    # Тестируем программу на некорректных данных. Функция вызывает исключение TypeError
    def test_with_char(self):
        with pytest.raises(ValueError):
            my_lib.calculator(1, 2, '[')

    def test_div_zero(self):
        with pytest.raises(ZeroDivisionError):
            my_lib.calculator(1, 0, '/')
