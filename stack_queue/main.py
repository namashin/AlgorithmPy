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


if __name__ == '__main__':
    stack = Stack()
    stack.push('No1')
    stack.push('No2')
    stack.push('No3')
    print(stack.pop())
    stack.print()

    queue = Queue()
    queue.push('No1')
    queue.push('No2')
    queue.push('No3')
    print(queue.pop())
    queue.print()
