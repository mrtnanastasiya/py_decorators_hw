import os
from datetime import datetime

def logger(old_function):

    def new_function(*args, **kwargs):
        res = old_function(*args, **kwargs)
        with open('iterators.log', 'a', encoding='utf-8') as file:
            file.write(
                f'Дата и время: {datetime.now()} \n'
                f'Название функции: {old_function.__name__} \n'
                f'Аргументы: {args}, {kwargs} \n'
                f'Функция вернула: {res}\n\n')
            file.close()
        return res

    return new_function

class FlatIterator:

    def __init__(self, list_of_list):
        self.main_list = list_of_list

    def __iter__(self):
        self.main_list_cursor = 0
        return self

    def __next__(self):
        obj = []
        for i in self.main_list:
            for j in i:
                obj += [j]

        if self.main_list_cursor < len(obj):
            res = obj[self.main_list_cursor]
            self.main_list_cursor += 1
            return res
        raise StopIteration

@logger
def test_1():
    path = 'iterators.log'
    if os.path.exists(path):
        os.remove(path)

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        return list(FlatIterator(list_of_lists_1))

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    assert os.path.exists(path), 'iterators.log должен существовать'

    with open(path) as log_file:
        log_file_content = log_file.read()


if __name__ == '__main__':
    test_1()