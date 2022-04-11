import hashlib


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
