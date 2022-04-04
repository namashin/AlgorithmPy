import unittest
from typing import Any

# これは collections.deque の実装


class Stack(object):

    def __init__(self):
        self.stack = []

    def push(self, data: Any):
        self.stack.append(data)

    def pop(self) -> Any:
        return self.stack.pop()

    def print(self):
        print(self.stack)


class Queue(object):

    def __init__(self):
        self.queue = []

    def push(self, data: Any):
        self.queue.append(data)

    def pop(self) -> Any:
        return self.queue.pop(0)

    def print(self):
        print(self.queue)


class TestStack(unittest.TestCase):

    def setUp(self) -> None:
        self.stack = Stack()

    def tearDown(self) -> None:
        pass

    def test_push(self):
        self.stack.push("No1")
        self.stack.push("No2")
        self.stack.push("No3")

        self.assertEqual("No1", self.stack.stack[0])
        self.assertEqual("No3", self.stack.stack[2])

    def test_pop(self):
        self.stack.push("No1")
        self.stack.push("No2")
        self.stack.push("No3")

        value = self.stack.pop()

        self.assertEqual(value, "No3")


class TestQueue(unittest.TestCase):

    def setUp(self) -> None:
        self.queue = Queue()

    def tearDown(self) -> None:
        pass

    def test_push(self):
        self.queue.push("No1")
        self.queue.push("No2")
        self.queue.push("No3")

        self.assertEqual("No1", self.queue.queue[0])
        self.assertEqual("No3", self.queue.queue[2])

    def test_pop(self):
        self.queue.push("No1")
        self.queue.push("No2")
        self.queue.push("No3")

        value = self.queue.pop()

        self.assertEqual(value, "No1")
        self.assertEqual(2, len(self.queue.queue))


# json形式を検証する関数
def validate_json(chars: str) -> bool:
    lookup = {'{': '}', '(': ')', '[': ']'}
    stack = []

    for char in chars:
        if char in lookup.keys():
            stack.append(lookup[char])

        if char in lookup.values():
            # pythonのlistは、空であればFalse、中身が入ってればTrueを返す性質があります。
            if stack is None:
                return False

            if char != stack.pop():
                return False

    if stack:
        """最終的にstackの中は空リスト: [] じゃないといけない"""
        return False

    return True


if __name__ == '__main__':
    unittest.main()
    # stack = Stack()
    # stack.push('No1')
    # stack.push('No2')
    # stack.push('No3')
    # print(stack.pop())
    # stack.print()
    #
    # queue = Queue()
    # queue.push('No1')
    # queue.push('No2')
    # queue.push('No3')
    # print(queue.pop())
    # queue.print()
    #
    # input = "{'key1': 'value1', 'key2': (1, 2, 3), 'key3': [1, 2]}"
    # print(validate_json(input))
