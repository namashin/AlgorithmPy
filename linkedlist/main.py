from __future__ import annotations
from typing import Any, Optional


# class Node(object):
#     def __init__(self, data: Any, next_node: Node = None):
#         self.data = data
#         self.next = next_node


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def append(self, data: Any) -> None:
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert(self, data: Any):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def print(self):
        all_nodes = self.head

        while all_nodes:
            print(all_nodes.data)
            all_nodes = all_nodes.next

    def remove(self, data: Any):
        current_node = self.head
        if current_node and current_node.data == data:
            # 先頭が削除したいdataだった時
            self.head = current_node.next
            current_node = None
            return

        previous_node = None
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        previous_node.next = current_node.next
        current_node = None

    def remove2(self, target: int) -> None:
        if self.head is None:
            return

        current = self.head
        if current and current.data == target:
            if current.next is None:
                self.head = None
                current = None
                return
            else:
                self.head = current.next
                current = None
                return

        previous = None
        while current and current.data != target:
            previous = current
            current = current.next

        if current is None:
            return

        if current.next is None:
            previous.next = None
            current = None
            return
        else:
            previous.next = current.next
            current = None
            return

    @staticmethod
    def get_next_node(node: Node) -> Any:
        return node.next.data

    def reverse_iterative(self):
        previous_node = None
        current_node = self.head

        while current_node:
            next_node = current_node.next
            current_node.next = previous_node

            previous_node = current_node
            current_node = next_node

        self.head = previous_node

    def reverse_recursive(self):
        def _reverse_recursive(current_node: Node, previous_node: Optional[Node]):
            if current_node is None:
                return previous_node

            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            return _reverse_recursive(current_node, previous_node)

        self.head = _reverse_recursive(self.head, None)
        return

    def sort(self):
        if self.head is None:
            return

        current = self.head
        while current:
            next_node = current.next
            while next_node:
                if current.data > next_node.data:
                    current.data, next_node.data = next_node.data, current.data
                next_node = next_node.next

            current = current.next
        return


class Node(object):
    def __init__(self, data: Any, prev: Node = None, next_node: Node = None):
        self.prev = prev
        self.data = data
        self.next = next_node


class DoublyLinkedList(object):

    def __init__(self, head: Node = None):
        self.head = head

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current

    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def insert(self, data: Any):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        # self.head にNodeがすでに入っている場合
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def remove(self, target: Any):
        current = self.head

        if current and current.data == target:
            # 先頭を消す場合で、先頭の次が何も入ってない場合
            if current.next is None:
                current = None
                self.head = None
                return
            else:
                # 先頭の次が何か入っている場合
                next = current.next
                next.prev = None
                current = None
                self.head = next
                return

        # 二番目以降を消す場合
        while current and current.data != target:
            current = current.next

        if current is None:
            return

        # targetが見つかって、その次がNoneの時
        if current.next is None:
            prev = current.prev
            prev.next = None
            current = None
            return
        else:
            # targetが見つかって、その次に何か入ってる場合
            next = current.next
            prev = current.prev
            prev.next = next
            next.prev = prev
            current = None
            return

    def reverse_iterative(self) -> None:
        previous = None
        current = self.head
        while current:
            previous = current.prev
            current.prev = current.next
            current.next = previous

            # appendの時は while current.next:
            # で次のnextがあるかどうか見ていた
            # 今回はreverseなので、nextではなく
            # prevがあるかを見ている。
            current = current.prev   

        if previous:
            self.head = previous.prev

    def reverse_recursive_1(self):
        def _reverse_recursive_1(current: Node):
            if current is None:
                return None

            prev = current.prev
            current.prev = current.next
            current.next = prev

            if current.prev is None:
                return current

            return _reverse_recursive_1(current.prev)

        self.head = _reverse_recursive_1(self.head)
        return

    def reverse_recursive_2(self):
        def _reverse_recursive_2(current: Node):
            previous = current.prev
            current.prev = current.next
            current.next = previous

            current = current.prev

            if current is None:
                return previous.prev

            return _reverse_recursive_2(current)

        self.head = _reverse_recursive_2(self.head)
        return

    def sort(self):
        if self.head is None:
            return

        current = self.head
        while current:
            next_node = current.next
            while next_node:
                if current.data > next_node.data:
                    current.data, next_node.data = next_node.data, current.data
                next_node = next_node.next

            current = current.next
        return
