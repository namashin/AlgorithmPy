import unittest
import main


class TestHashTable(unittest.TestCase):

    def setUp(self) -> None:
        self.hash_table = main.HashTable()

    def tearDown(self) -> None:
        pass

    def test_hash(self):
        key1 = "my_key"
        key2 = "my_key"

        hash_num1 = self.hash_table.hash(key1)
        hash_num2 = self.hash_table.hash(key2)

        self.assertEqual(hash_num1, hash_num2)

    def test_add(self):
        self.hash_table.add("key1", "value1")
        self.hash_table.add("key2", "value2")
        self.hash_table.add("key1", "value3")

        hash_num1 = self.hash_table.hash("key1")

        self.assertIsInstance(self.hash_table.table[hash_num1][0], list)
        self.assertEqual(self.hash_table.table[hash_num1][0][1], "value3")

    def test_get(self):
        self.hash_table.add("key1", "value1")
        self.hash_table.add("key2", "value2")

        value = self.hash_table.get("key1")

        self.assertEqual(value, "value1")


if __name__ == '__main__':
    unittest.main()
