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

    def test_max_depth(self):
        depth = self.bst.max_depth()
        self.assertEqual(depth, 4)

    def test_size_recursive(self):
        size = self.bst.size_recursive()
        self.assertEqual(size, 6)

    def test_insert(self):
        top_value = self.bst.root.value
        self.assertEqual(top_value, 3)

        top_left_value = self.bst.root.left.value
        self.assertEqual(top_left_value, 1)

        top_right_value = self.bst.root.right.value
        self.assertEqual(top_right_value, 6)

        top_right_left_value = self.bst.root.right.left.value
        self.assertEqual(top_right_left_value, 5)

        top_right_right_value = self.bst.root.right.right.value
        self.assertEqual(top_right_right_value, 7)

        top_right_right_right_value = self.bst.root.right.right.right.value
        self.assertEqual(top_right_right_right_value, 10)

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

    def test_get_biggest_node(self):
        node = self.bst.root
        biggest_node = self.bst.get_biggest_node(node)

        self.assertEqual(biggest_node.value, 10)

    def test_validate_bst(self):
        self.assertTrue(self.bst.validate_bst())

    def test_inorder_generate(self):
        nodes = self.bst.inorder_generate(self.bst.root)
        self.assertEqual(nodes.__next__(), 1)
        self.assertEqual(nodes.__next__(), 3)
        self.assertEqual(nodes.__next__(), 5)
        self.assertEqual(nodes.__next__(), 6)
        self.assertEqual(nodes.__next__(), 7)
        self.assertEqual(nodes.__next__(), 10)

        # for i, node_value in enumerate(self.bst.inorder_generate(self.bst.root)):
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


class TestMiniHeap(unittest.TestCase):
    def setUp(self) -> None:
        self.min_heap = main.MiniHeap()

    def tearDown(self) -> None:
        pass

    def test_push(self):
        self.min_heap.push(10)
        self.min_heap.push(8)
        self.min_heap.push(4)
        self.min_heap.push(7)
        self.min_heap.push(3)
        self.min_heap.push(1)

        for i, num in enumerate(self.min_heap.heap):
            if i == 1:
                self.assertEqual(self.min_heap.heap[1], 1)
            elif i == 2:
                self.assertEqual(self.min_heap.heap[2], 4)
            elif i == 3:
                self.assertEqual(self.min_heap.heap[3], 3)
            elif i == 4:
                self.assertEqual(self.min_heap.heap[4], 10)
            elif i == 5:
                self.assertEqual(self.min_heap.heap[5], 7)
            elif i == 6:
                self.assertEqual(self.min_heap.heap[6], 8)

    def test_pop(self):
        # Init
        self.min_heap.push(10)
        self.min_heap.push(8)
        self.min_heap.push(4)
        self.min_heap.push(7)
        self.min_heap.push(3)
        self.min_heap.push(1)

        # Execute
        self.min_heap.pop()

        # Validation
        for i, num in enumerate(self.min_heap.heap):
            if i == 1:
                self.assertEqual(self.min_heap.heap[1], 3)
            elif i == 2:
                self.assertEqual(self.min_heap.heap[2], 4)
            elif i == 3:
                self.assertEqual(self.min_heap.heap[3], 8)
            elif i == 4:
                self.assertEqual(self.min_heap.heap[4], 10)
            elif i == 5:
                self.assertEqual(self.min_heap.heap[5], 7)


if __name__ == '__main__':
    unittest.main()
