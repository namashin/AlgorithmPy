import unittest
import main


class TestBinarySearchTree(unittest.TestCase):

    def setUp(self) -> None:
        self.bst = main.BinarySearchTree()

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

    def test_get_minimum_node(self):
        node = self.bst.root
        min_node = self.bst.get_minimum_node(node)

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
