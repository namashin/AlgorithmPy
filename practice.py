from __future__ import annotations
import random
import unittest
from typing import List, Tuple, Any


class Node(object):

    def __init__(self, data: Any, next_node: Node = None):
        self.data = data
        self.node = next_node


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def append(self, data: Any):
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


class TestLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.linked_list = LinkedList()

    def tearDown(self) -> None:
        pass

    def test_append(self):
        self.linked_list.append("Test1")
        self.assertEqual("Test1", self.linked_list.head.data)

    def test_insert(self):
        self.linked_list.insert("Test2")
        self.assertEqual("Test2", self.linked_list.head.data)




if __name__ == '__main__':
    unittest.main()
