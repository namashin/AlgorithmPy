from __future__ import annotations
from typing import Any, Optional


# 一方向リンクリスト用のノードクラス
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

    def remove_element(self, target: Any) -> None:
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

    def remove_elements(self, target):
        """
        片方向リンクリストの場合、class Node（ノード）に　prev　が無いので、
        変数: previousが必要
        """
        if not self.head:
            return

        def _remove_elements(head: Node, _target: Any) -> Optional[Node]:
            previous = None
            current = head

            while current:
                if current.data == _target:
                    if previous:
                        previous.next = current.next
                    else:
                        head = current.next

                    current = current.next

                else:
                    previous = current
                    current = current.next

            return head

        self.head = _remove_elements(self.head, target)

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

    def sort(self):
        current = self.head
        while current:
            next_node = current.next
            while next_node:
                if current.data > next_node.data:
                    current.data, next_node.data = next_node.data, current.data
                next_node = next_node.next

            current = current.next

    def is_palindrome(self) -> bool:
        if self.head is None:
            return False

        current = self.head
        node_list = []
        while current:
            node_list.append(current.data)
            current = current.next

        return node_list == node_list[::-1]


# 双方向リンクリスト用のノードクラス
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

    def remove_element(self, target: Any) -> None:
        """
        最初のtargetのみ削除

        :param target: 削除する値
        :return:
        """
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

        # targetが見つかって、その次がNoneの時（最後尾）
        if current.next is None:
            prev = current.prev
            prev.next = None
            current = None
        else:
            # targetが見つかって、その次に何か入ってる場合
            next = current.next
            prev = current.prev
            prev.next = next
            next.prev = prev
            current = None

    def remove_elements(self, target: Any) -> None:
        """
        全てのtarget値を削除

        :param target: 削除する値
        :return:
        """

        current = self.head
        previous = None

        while current:
            if current.data == target:
                if previous:
                    previous.next = current.next
                else:
                    # headの一番先頭が削除する値の時
                    self.head = current.next

                current = current.next

            else:
                previous = current
                current = current.next

    # 単方向リンクリストのリバース方法でも可
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

    def sort(self):
        current = self.head
        while current:
            next_node = current.next
            while next_node:
                if current.data > next_node.data:
                    current.data, next_node.data = next_node.data, current.data
                next_node = next_node.next

            current = current.next
