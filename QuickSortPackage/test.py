from QuickSortPackage.source import quick_sort
import pytest


def test_fine_list():
    assert quick_sort([10, 0, 0, -1, 15, -3, -3]) == [-3, -3, -1, 0, 0, 10, 15]


def test_list_with_inner_list():
    with pytest.raises(TypeError):
        quick_sort([[]])


def test_empty_list():
    assert quick_sort([]) == []


def test_sorted_list():
    assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_list_of_one():
    assert quick_sort([1]) == [1]


def test_not_int():
    with pytest.raises(TypeError):
        quick_sort([1, 0.5])
