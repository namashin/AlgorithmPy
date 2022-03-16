import unittest
from typing import List, NewType

Index = NewType("index", int)


def binary_search(numbers: List[int], target: int) -> Index:
    left, right = 0, len(numbers) - 1

    while left <= right:

        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid

        elif numbers[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


def binary_search_recursive(numbers: List[int], target: int) -> Index:
    def _binary_search_recursive(numbers: List[int], target: int, left: int, right: int) -> Index:

        if left > right:
            return -1

        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid

        elif numbers[mid] < target:
            return _binary_search_recursive(numbers, target, mid + 1, right)

        else:
            return _binary_search_recursive(numbers, target, left, mid - 1)

    return _binary_search_recursive(numbers, target, 0, len(numbers) - 1)


class TestSearch(unittest.TestCase):

    def setUp(self) -> None:
        self.numbers = [1, 3, 5, 6, 7, 9, 10, 22]
        self.target = 9
        self.wrong_target = 100

    def tearDown(self) -> None:
        pass

    def test_binary_search(self):
        ret = binary_search(self.numbers, self.target)
        ret1 = binary_search(self.numbers, self.wrong_target)

        target_index = 5

        self.assertEqual(target_index, ret)
        self.assertEqual(-1, ret1)

    def test_binary_search_recursive(self):
        ret = binary_search_recursive(self.numbers, self.target)
        ret1 = binary_search_recursive(self.numbers, self.wrong_target)

        target_index = 5
        self.assertEqual(target_index, ret)
        self.assertEqual(-1, ret1)


if __name__ == '__main__':
    # 既にソートされ終わった事を想定
    # その後、目的の数字のインデックスを取得
    unittest.main()
