from typing import Any


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


# json形式を検証する関数
def validate_json(chars: str) -> bool:
    lookup = {'{': '}', '(': ')', '[': ']'}
    stack = []

    for char in chars:
        if char in lookup.keys():
            stack.append(lookup[char])

        if char in lookup.values():
            if not stack:
                return False

            if char != stack.pop():
                return False

    if stack:
        """最終的にstackの中は空じゃないといけない"""
        return False

    return True


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

    input = "{'key1': 'value1', 'key2': (1, 2, 3), 'key3': [1, 2]}"
    print(validate_json(input))
