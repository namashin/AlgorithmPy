from typing import Optional


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
    """
    left -> top -> right
    :param node: バイナリーサーチノード
    """
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
        # node.value == valueの時
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
        if self.root is None:
            self.root = Node(value)
            return

        def _insert(node: Node, value: int) -> Node:
            if node is None:
                return Node(value)

            if value < node.value:
                node.left = _insert(node.left, value)
            elif value > node.value:
                node.right = _insert(node.right, value)
            return node
        _insert(self.root, value)

    def inorder(self):
        def _inorder(node: Node):
            if node:
                _inorder(node.left)
                print(node.value)
                _inorder(node.right)
        _inorder(self.root)

    def inorder2(self, node: Node):
        if node:
            yield from self.inorder2(node.left)
            yield node.value
            yield from self.inorder2(node.right)

    def search(self, target: int):
        def _search(node: Node, target: int) -> bool:
            if node is None:
                return False

            if node.value == target:
                return True
            elif node.value > target:
                return _search(node.left, target)
            elif node.value < target:
                return _search(node.right, target)

        print(_search(self.root, target))

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

    def remove(self, target: int) -> None:
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

        _remove(self.root, target)
