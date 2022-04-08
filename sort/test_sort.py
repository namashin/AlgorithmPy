import unittest
import random
import main


class TestSorts(unittest.TestCase):

    def setUp(self) -> None:
        self.nums = [random.randint(0, 100) for _ in range(10)]

    def tearDown(self) -> None:
        pass

    def test_bubble_sort(self):
        main.bubble_sort(self.nums)

        for i, num in enumerate(self.nums):
            try:
                # self.nums[i + 1] >= num
                self.assertGreaterEqual(self.nums[i + 1], num)
            except IndexError:
                continue

    def test_selection_sort(self):
        main.selection_sort(self.nums)

        for i, num in enumerate(self.nums):
            try:
                # self.nums[i + 1] >= num
                self.assertGreaterEqual(self.nums[i + 1], num)
            except IndexError:
                continue

    def test_insertion_sort(self):
        main.insertion_sort(self.nums)

        for i, num in enumerate(self.nums):
            try:
                # self.nums[i + 1] >= num
                self.assertGreaterEqual(self.nums[i + 1], num)
            except IndexError:
                continue


if __name__ == '__main__':
    unittest.main()
