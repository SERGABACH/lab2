def fibonacci_numbers(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for _ in range(2, n):
            next_number = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_number)
        return fib_sequence


def bubble_sort(input_list):
    # Создаем копию входного списка, чтобы не изменять исходный список
    sorted_list = input_list.copy()

    n = len(sorted_list)
    for i in range(n):
        # Флаг, который позволяет оптимизировать сортировку.
        # Если на текущей итерации не было обменов, то список уже отсортирован.
        swapped = False

        for j in range(0, n - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                # Меняем местами элементы, если текущий больше следующего
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
                swapped = True

        # Если на текущей итерации не было обменов, то список уже отсортирован
        if not swapped:
            break

    return sorted_list


def calculator(num1, num2, operator):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("Ошибка: деление на ноль")
        result = num1 / num2
    else:
        raise ValueError("Неверный оператор")

    return result
