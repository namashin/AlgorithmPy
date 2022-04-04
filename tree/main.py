import unittest


class Node(object):

    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
        
        
# 関数ver ------------------------------------------        
def insert(node: Node, value: int) -> Node:
    if node is None:
        return Node(value)

    if value > node.value:
        node.right = insert(node.right, value)
    elif value < node.value:
        node.left = insert(node.left, value)
    return node


# left -> top -> right
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


def min_value(node: Node) -> Node:
    current = node
    while current.left:
        current = current.left
    return current


def remove(node: Node, value: int) -> Node:
    if node is None:
        return node

    if value > node.value:
        node.right = remove(node.right, value)
    elif value < node.value:
        node.left = remove(node.left, value)
    else:
        # node.value == value
        if node.left is None:
            return node.right

        elif node.right is None:
            return node.left

        temp = min_value(node.right)
        node.value = temp.value
        node.right = remove(node.right, temp.value)
    return node

# 関数ver End ----------------------------------------------


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

    # inorder: left -> node -> rightの順に見ていく
    # 小さい順に表示
    def inorder(self):
        def _inorder(node: Node):
            if node:
                _inorder(node.left)
                print(node.value)
                _inorder(node.right)
        _inorder(self.root)

    def inorder2(self, node: Node):
        if node is not None:
            yield from self.inorder2(node.left)
            yield node.value
            yield from self.inorder2(node.right)

    def search(self, target: int) -> bool:
        def _search(node: Node, target: int) -> bool:
            if node is None:
                return False

            if node.value == target:
                return True

            elif node.value > target:
                return _search(node.left, target)
            elif node.value < target:
                return _search(node.right, target)
        return _search(self.root, target)

    def min_value(self, node: Node) -> Node:
        current = node
        while current.left is not None:
            current = current.left
        return current

    def remove(self, target: int) -> None:
        def _remove(node: Node, target: int) -> Node:
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

                temp = self.min_value(node.right)
                node.value = temp.value
                node.right = _remove(node.right, temp.value)
            return node

        _remove(self.root, target)


class TestBinarySearchTree(unittest.TestCase):

    def setUp(self) -> None:
        self.bst = BinarySearchTree()

        self.bst.insert(3)
        self.bst.insert(6)
        self.bst.insert(5)
        self.bst.insert(7)
        self.bst.insert(1)
        self.bst.insert(10)

    def tearDown(self) -> None:
        pass

    def test_insert(self):
        top_value = self.bst.root.value
        self.assertEqual(top_value, 3)

        top_left_value = self.bst.root.left.value
        self.assertEqual(top_left_value, 1)

        top_right_left_value = self.bst.root.right.left.value
        self.assertEqual(top_right_left_value, 5)

    def test_search(self):
        is_there = self.bst.search(7)
        self.assertTrue(is_there)

        is_there = self.bst.search(100)
        self.assertFalse(is_there)

    def test_remove(self):
        top_left_value = self.bst.root.left.value
        is_there = self.bst.search(top_left_value)
        self.assertTrue(is_there)

        self.bst.remove(1)

        is_there = self.bst.search(top_left_value)
        self.assertFalse(is_there)

    def test_min_value(self):
        node = self.bst.root
        min_node = self.bst.min_value(node)

        self.assertEqual(min_node.value, 1)

    def test_inorder2(self):
        nodes = self.bst.inorder2(self.bst.root)
        self.assertEqual(nodes.__next__(), 1)
        self.assertEqual(nodes.__next__(), 3)
        self.assertEqual(nodes.__next__(), 5)
        self.assertEqual(nodes.__next__(), 6)
        self.assertEqual(nodes.__next__(), 7)
        self.assertEqual(nodes.__next__(), 10)

        # for i, node_value in enumerate(self.bst.inorder2(self.bst.root)):
        #     if i == 0:
        #         self.assertEqual(node_value, 1)
        #     elif i == 1:
        #         self.assertEqual(node_value, 3)
        #     elif i == 2:
        #         self.assertEqual(node_value, 5)
        #     elif i == 3:
        #         self.assertEqual(node_value, 6)
        #     elif i == 4:
        #         self.assertEqual(node_value, 7)
        #     elif i == 5:
        #         self.assertEqual(node_value, 10)
        #     else:
        #         self.fail()


if __name__ == '__main__':
    unittest.main()
