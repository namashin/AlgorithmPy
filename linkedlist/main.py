from __future__ import annotations
import unittest
from typing import Any


# class Node(object):
#     def __init__(self, data: Any, next_node: Node = None):
#         self.data = data
#         self.next = next_node


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    # 一番後ろに追加
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
        """
        先頭に追加
        :param data: 追加するデータ
        """
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

    def get_next_node(self, node: Node) -> Any:
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
        def _reverse_recursive(current_node: Node, previous_node: Node):
            if not current_node:  # if current_node is None
                return previous_node

            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            return _reverse_recursive(current_node, previous_node)

        self.head = _reverse_recursive(self.head, None)


class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.linked_list = LinkedList()

    def tearDown(self) -> None:
        pass

    def test_append(self):
        self.linked_list.append("Test1")
        self.linked_list.append("Test2")
        self.linked_list.append("Test3")

        self.assertEqual("Test1", self.linked_list.head.data)
        self.assertEqual("Test2", self.linked_list.head.next.data)
        self.assertEqual("Test3", self.linked_list.head.next.next.data)

    def test_insert(self):
        self.linked_list.append("Test1")
        self.linked_list.append("Test2")
        self.linked_list.append("Test3")

        self.linked_list.insert("Test4")
        self.assertEqual("Test4", self.linked_list.head.data)

    def test_remove(self):
        self.linked_list.append("Test1")
        self.linked_list.append("Test2")

        self.linked_list.remove("Test1")
        self.assertEqual("Test2", self.linked_list.head.data)

    def test_reverse_iterative(self):
        self.linked_list.append("Test1")
        self.linked_list.append("Test2")
        self.linked_list.append("Test3")

        self.linked_list.reverse_iterative()

        self.assertEqual("Test3", self.linked_list.head.data)
        self.assertEqual("Test2", self.linked_list.head.next.data)
        self.assertEqual("Test1", self.linked_list.head.next.next.data)

    def test_reverse_recursive(self):
        self.linked_list.append("Test1")
        self.linked_list.append("Test2")
        self.linked_list.append("Test3")

        self.linked_list.reverse_recursive()

        self.assertEqual("Test3", self.linked_list.head.data)
        self.assertEqual("Test2", self.linked_list.head.next.data)
        self.assertEqual("Test1", self.linked_list.head.next.next.data)


class Node(object):
    def __init__(self, data: Any, prev: Node = None, next_node: Node = None):
        self.prev = prev
        self.data = data
        self.next = next_node


class DoublyLinkedList(object):

    def __init__(self, head=None):
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
        new_node.next = self.head
        self.head = new_node

    def remove(self, target: Any):
        current = self.head
        # 先頭を消す場合
        if current and current.data == target:
            # 先頭の次が何も入ってない場合
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

        elif current is None:
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


class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.doubly_linked_list = DoublyLinkedList()

    def tearDown(self) -> None:
        pass

    def test_append(self):
        self.doubly_linked_list.append(1)
        self.doubly_linked_list.append(2)
        self.doubly_linked_list.append(3)

        self.assertEqual(1, self.doubly_linked_list.head.data)
        self.assertEqual(2, self.doubly_linked_list.head.next.data)
        self.assertEqual(3, self.doubly_linked_list.head.next.next.data)

        self.assertEqual(2, self.doubly_linked_list.head.next.next.prev.data)
        self.assertEqual(1, self.doubly_linked_list.head.next.next.prev.prev.data)

    def test_insert(self):
        self.doubly_linked_list.append(1)
        self.doubly_linked_list.append(2)
        self.doubly_linked_list.append(3)

        self.doubly_linked_list.insert(5)

        self.assertEqual(5, self.doubly_linked_list.head.data)

    def test_remove(self):
        self.doubly_linked_list.append(1)
        self.doubly_linked_list.append(2)
        self.doubly_linked_list.append(3)

        self.doubly_linked_list.remove(2)

        self.assertEqual(1, self.doubly_linked_list.head.data)
        self.assertEqual(3, self.doubly_linked_list.head.next.data)


if __name__ == '__main__':
    unittest.main()
