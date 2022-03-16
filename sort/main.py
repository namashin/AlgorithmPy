import random
import unittest
from typing import List


def bubble_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)

    for i in range(len_numbers):
        for j in range(len_numbers - 1 - i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


def selection_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)

    for i in range(len_numbers):
        min_index = i

        for j in range(i+1, len_numbers):
            if numbers[min_index] > numbers[j]:
                min_index = j
        numbers[min_index], numbers[i] = numbers[i], numbers[min_index]

    return numbers


def insertion_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)

    for i in range(1, len_numbers):
        temp = numbers[i]
        j = i - 1
        while j >= 0 and temp < numbers[j]:
            numbers[j+1] = numbers[j]
            j -= 1

        numbers[j+1] = temp

    return numbers


class TestSorts(unittest.TestCase):

    def setUp(self) -> None:
        self.nums = [random.randint(0, 100) for _ in range(10)]

    def tearDown(self) -> None:
        pass

    def test_bubble_sort(self):
        bubble_sort(self.nums)

        for i, num in enumerate(self.nums):
            try:
                # self.nums[i + 1] >= num
                self.assertGreaterEqual(self.nums[i + 1], num)
            except IndexError:
                continue

    def test_selection_sort(self):
        selection_sort(self.nums)

        for i, num in enumerate(self.nums):
            try:
                # self.nums[i + 1] >= num
                self.assertGreaterEqual(self.nums[i + 1], num)
            except IndexError:
                continue

    def test_insertion_sort(self):
        insertion_sort(self.nums)

        for i, num in enumerate(self.nums):
            try:
                # self.nums[i + 1] >= num
                self.assertGreaterEqual(self.nums[i + 1], num)
            except IndexError:
                continue


if __name__ == '__main__':
    unittest.main()
