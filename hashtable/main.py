import hashlib
import unittest

from typing import NewType, Tuple, List, Iterator

# hashTableKey = NewType('hash table key', int)


class HashTable(object):

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash(self, key: str) -> int:
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size

    def add(self, key: str, value: str):
        index = self.hash(key)

        for data in self.table[index]:
            if data[0] == key:
                data[1] = value
                return

        else:
            self.table[index].append([key, value])

    def delete(self, key: str):
        index = self.hash(key)

        for data in self.table[index]:
            if data[0] == key:
                data.clear()
                break

    def get(self, key: str):
        index = self.hash(key)

        for data in self.table[index]:
            if data[0] == key:
                return data[1]

    def __setitem__(self, key, value):
        return self.add(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def print(self):
        for data in self.table:
            print(data, end='')

            print()


class TestHashTable(unittest.TestCase):

    def setUp(self) -> None:
        self.hash_table = HashTable()

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


# [(1, 2), (3, 5), (4, 7), (5, 3), (7, 4)]
# の中から、対になっているものを探す
def find_pair(pairs: List[Tuple[int, int]]) -> Iterator[Tuple[int, int]]:
    cache = dict()

    for pair in pairs:
        first, second = pair[0], pair[1]
        value = cache.get(second)
        if not value:
            """valueが取れなかったら、Noneがvalueに入る"""
            cache[first] = second
            
        elif value == first:
            yield pair


# input = [(1, 2), (3, 5), (4, 7), (5, 3), (7, 4)]
# for pair in find_pair(input):
# print(pair)
            

"""
キャッシュデコレーターの生成
"""


def memoize(f):
    cache = dict()

    def _wrapper(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return _wrapper


@memoize
def cpu_bound(num: int) -> int:
    x = 0
    for i in range(100000):
        x += num * i
    return x


if __name__ == '__main__':
    print(cpu_bound(4))
    print(cpu_bound(4))

    # hash_table = HashTable()
    # hash_table.add('pc', 'mac')
    # hash_table.add('phone', 'iPhone')
    # hash_table.add('phone', 'sumsung')
    # hash_table.add('car', 'toyota')
    # hash_table.add('sns', 'youtube')
    #
    # hash_table['os'] = 'windows'
    #
    # hash_table.print()
    # print("############")
    # hash_table.delete('pc')
    # hash_table.delete('car')
    # hash_table.print()
    #
    # print(hash_table['os'])
