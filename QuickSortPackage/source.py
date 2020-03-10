import random


def quick_sort(list_to_sort):
    """
    Быстрая сортировка списка.
    Функция сортирует полученный список методом быстрой
    сортировки и возвращает отсортированный список.
    >>> quick_sort([10, 0, 0, -1, 15, -3, -3])
    [-3, -3, -1, 0, 0, 10, 15]
    >>> quick_sort([])
    []
    >>> quick_sort([[]])
    Traceback (most recent call last):
    ...
    TypeError: List contains something but int type
    >>> quick_sort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> quick_sort([1])
    [1]
    >>> quick_sort([1, 0.5])
    Traceback (most recent call last):
    ...
    TypeError: List contains something but int type
    """
    for i in list_to_sort:
        if not isinstance(i, int):
            raise TypeError("List contains something but int type")

    if len(list_to_sort) <= 1:
        return list_to_sort
    chosen_element = list_to_sort[random.randint(0, len(list_to_sort) - 1)]
    left_part = list()
    right_part = list()
    middle_part = list()
    for i in list_to_sort:
        if i < chosen_element:
            left_part.append(i)
        if i > chosen_element:
            right_part.append(i)
        if i == chosen_element:
            middle_part.append(i)
    return quick_sort(left_part) + middle_part + quick_sort(right_part)
