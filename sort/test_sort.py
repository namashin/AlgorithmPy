import unittest
import random
import main


class TestSorts(unittest.TestCase):

    def setUp(self) -> None:
        self.nums = [random.randint(0, 1000) for _ in range(10)]

    def tearDown(self) -> None:
        pass

    def test_bubble_sort(self):
        main.bubble_sort(self.nums)

        prev = 0
        for num in self.nums:
            # prev <= num
            self.assertLessEqual(prev, num)
            prev = num

    def test_selection_sort(self):
        main.selection_sort(self.nums)

        prev = 0
        for num in self.nums:
            self.assertLessEqual(prev, num)
            prev = num

    def test_insertion_sort(self):
        main.insertion_sort(self.nums)

        prev = 0
        for num in self.nums:
            self.assertLessEqual(prev, num)
            prev = num

    def test_quick_sort(self):
        main.quick_sort(self.nums)
        prev = 0
        for num in self.nums:
            self.assertLessEqual(prev, num)
            prev = num


if __name__ == '__main__':
    unittest.main()
