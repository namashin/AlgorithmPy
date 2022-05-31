from typing import Optional
import heapq
import sys


class Node(object):

    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def insert(node: Node, value: int) -> Node:
    if node is None:
        return Node(value)

    if value > node.value:
        node.right = insert(node.right, value)
    elif value < node.value:
        node.left = insert(node.left, value)
    return node


def inorder(node: Node):
    if node:
        inorder(node.left)
        print(node.value)
        inorder(node.right)


def search(node: Node, target: int) -> bool:
    if node is None:
        return False

    if target == node.value:
        return True

    elif target > node.value:
        return search(node.right, target)

    elif target < node.value:
        return search(node.left, target)


def get_minimum_node(node: Node) -> Node:
    current = node
    while current.left:
        current = current.left
    return current


def get_biggest_node(node: Node) -> Node:
    current = node
    while current.right:
        current = current.right
    return current


def remove(node: Node, value: int) -> Optional:
    if node is None:
        return node

    if value > node.value:
        node.right = remove(node.right, value)
    elif value < node.value:
        node.left = remove(node.left, value)
    else:
        # ３パターン（子ノード無し、片方のみノード有り、両方ノード有り）
        if node.left is None:
            return node.right

        elif node.right is None:
            return node.left

        temp = get_minimum_node(node.right)
        node.value = temp.value
        node.right = remove(node.right, temp.value)
    return node


class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def insert(self, value: int) -> None:
        def _insert(node: Node, _value: int) -> Node:
            if node is None:
                return Node(value)

            if value < node.value:
                node.left = _insert(node.left, _value)
            elif value > node.value:
                node.right = _insert(node.right, _value)
            return node

        self.root = _insert(self.root, value)

    def inorder(self):
        def _inorder(node: Node):
            if node:
                _inorder(node.left)
                print(node.value)
                _inorder(node.right)
        _inorder(self.root)

    def inorder_generate(self, node: Node):
        if node:
            yield from self.inorder_generate(node.left)
            yield node.value
            yield from self.inorder_generate(node.right)

    def validate_bst(self) -> bool:
        node_values = []
        for data in self.inorder_generate(self.root):
            node_values.append(data)

        i = len(node_values) - 1
        while 0 < i:
            if node_values[i] < node_values[i - 1]:
                return False

            i -= 1

        return True

    def search(self, search_target: int) -> bool:
        def _search(node: Node, target: int) -> bool:
            if node is None:
                return False

            if node.value == target:
                return True
            elif node.value > target:
                return _search(node.left, target)
            elif node.value < target:
                return _search(node.right, target)

        # print(_search(self.root, target))
        return _search(self.root, search_target)

    @staticmethod
    def get_minimum_node(node: Node) -> Node:
        current = node
        while current.left:
            current = current.left
        return current

    @staticmethod
    def get_biggest_node(node: Node) -> Node:
        current = node
        while current.right:
            current = current.right
        return current

    def remove(self, remove_target: int) -> None:
        def _remove(node: Node, target: int) -> Optional:
            if node is None:
                return node

            if target < node.value:
                node.left = _remove(node.left, target)
            elif target > node.value:
                node.right = _remove(node.right, target)
            else:
                if node.left is None:
                    return node.right
                elif target > node.value:
                    return node.left
                else:
                    temp = BinarySearchTree.get_minimum_node(node.right)
                    node.value = temp.value
                    node.right = _remove(node.right, temp.value)
            return node

        self.root = _remove(self.root, remove_target)


class MiniHeap(object):
    def __init__(self):
        self.heap = [-1 * sys.maxsize]
        self.current_size = 0

    @staticmethod
    def get_parent_index(index) -> int:
        return index // 2

    @staticmethod
    def get_left_child_index(index) -> int:
        return 2 * index

    @staticmethod
    def get_right_child_index(index) -> int:
        return (2 * index) + 1

    def swap(self, index1: int, index2: int) -> None:
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def heapify_up(self, index: int) -> None:
        while 0 < MiniHeap.get_parent_index(index):
            if self.heap[index] < self.heap[MiniHeap.get_parent_index(index)]:
                self.swap(index, MiniHeap.get_parent_index(index))
            index = MiniHeap.get_parent_index(index)

    def push(self, value: int) -> None:
        self.heap.append(value)
        self.current_size += 1
        self.heapify_up(self.current_size)

    def min_child(self, index: int) -> int:
        if self.heap[MiniHeap.get_left_child_index(index)] < self.heap[MiniHeap.get_right_child_index(index)]:
            return MiniHeap.get_left_child_index(index)

        else:
            return MiniHeap.get_right_child_index(index)

    def heapify_down(self, index: int):
        while MiniHeap.get_left_child_index(index) <= self.current_size:
            min_child_index = self.min_child(index)
            if self.heap[index] > self.heap[min_child_index]:
                self.swap(index, min_child_index)
            index = min_child_index

    def pop(self) -> Optional[int]:
        if len(self.heap) == 1:
            return

        root = self.heap[0]
        data = self.heap.pop()
        if len(self.heap) == 1:
            return root

        self.heap[1] = data
        self.current_size -= 1
        self.heapify_down(1)
        return root


if __name__ == '__main__':
    # heap の実装
    a = [7, 5, 3, 2, 4, 8, 10, 1]
    heapq.heapify(a)
    heapq.heappush(a, 6)
    heapq.heappop(a)
    print(a)
