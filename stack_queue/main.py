from typing import Any
from collections import deque


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


# collections.deque のreverseメソッドの実装
def reverse(d: deque) -> deque:
    new_deque = deque()
    while d:
        new_deque.append(d.pop())
    return new_deque
