import sys
import argparse
import random
import pytest
import source


def create_parser():
    local_parser = argparse.ArgumentParser()
    local_parser.add_argument("-test", dest="test", help="Выполнить тесты",
                              default=False, action="store_true")
    local_parser.add_argument("-n", type=int,
                              help="Каоличество элементов в массиве",
                              default=10)
    return local_parser


def main(args):
    parser = create_parser()
    arguments = parser.parse_args(args)
    if arguments.test:
        pytest.main(["-v", r"QuickSortPackage/test.py"])
        return
    list_to_sort = list()
    n = arguments.n
    string_to_output = ""
    for i in range(n):
        list_to_sort.append(random.randint(-10, 10))
        string_to_output += str(list_to_sort[i]) + " "
    print(string_to_output)
    list_to_sort = source.quick_sort(list_to_sort)
    string_to_output = ""
    for i in list_to_sort:
        string_to_output += str(i) + " "
    print(string_to_output)


if __name__ == "__main__":
    main(sys.argv[1:])
