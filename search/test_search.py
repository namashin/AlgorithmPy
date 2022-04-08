import unittest
import main


class TestSearch(unittest.TestCase):

    def setUp(self) -> None:
        self.numbers = [1, 3, 5, 6, 7, 9, 10, 22]
        self.target = 9
        self.wrong_target = 100

    def tearDown(self) -> None:
        pass

    def test_binary_search(self):
        ret = main.binary_search(self.numbers, self.target)
        ret1 = main.binary_search(self.numbers, self.wrong_target)

        target_index = 5

        self.assertEqual(target_index, ret)
        self.assertEqual(-1, ret1)

    def test_binary_search_recursive(self):
        ret = main.binary_search_recursive(self.numbers, self.target)
        ret1 = main.binary_search_recursive(self.numbers, self.wrong_target)

        target_index = 5
        self.assertEqual(target_index, ret)
        self.assertEqual(-1, ret1)


if __name__ == '__main__':
    unittest.main()
