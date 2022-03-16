from __future__ import annotations
import unittest
from typing import Any


class Node(object):
    """

    このNodeクラスが連結していく

    """

    def __init__(self, data: Any, next_node: Node = None):
        self.data = data
        self.next = next_node


class LinkedList(object):

    """

    先頭のheadにはまずNoneが入る

    """

    def __init__(self, head=None):
        self.head = head

    def append(self, data: Any) -> None:
        new_node = Node(data)

        if self.head is None:
            # 一番最初のみココはいる
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            """
            
            last_node.nextがNoneになったら抜けて、
            new_nodeをそこに入れる。
            
            nextにNodeを付けていく

            """
            last_node = last_node.next
        last_node.next = new_node

    def insert(self, data: Any):
        """
        new_nodeで先頭に挿入するノードを新規作成

        そのNodeのnextに今までのノード列のself.headを連結
        そして、self.headに先頭に挿入するnew_nodeを入れる

        new_node.dataにはinsert引数のdata: Anyが入っている。

        :param data: gonna append data
        :return: None
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
            if not current_node:
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


if __name__ == '__main__':
    unittest.main()
    # linked_list = LinkedList()
    # linked_list.append('No1')
    # linked_list.append('No2')
    # linked_list.append('No3')
    # linked_list.insert('No4')
    # linked_list.remove('No3')
    #
    # linked_list.reverse_iterative()
    # linked_list.print()
    # linked_list.reverse_recursive()
    # linked_list.print()
    #
    # print(linked_list.get_next_node(linked_list.head))
