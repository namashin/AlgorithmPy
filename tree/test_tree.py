import unittest
import main
import pytest


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

    def test_is_same_tree(self):
        # Init
        bst1 = main.BinarySearchTree()
        bst1.insert(5)
        bst1.insert(3)
        bst1.insert(7)
        bst1.insert(9)

        bst2 = main.BinarySearchTree()
        bst2.insert(5)
        bst2.insert(3)
        bst2.insert(7)
        bst2.insert(9)

        # Execution
        got = self.bst.is_same_tree(bst1.root, bst2.root)
        # Validation
        self.assertTrue(got)

    def test_is_same_tree_fail(self):
        # Init
        bst1 = main.BinarySearchTree()
        bst1.insert(5)
        bst1.insert(3)
        bst1.insert(7)
        bst1.insert(4)

        bst2 = main.BinarySearchTree()
        bst2.insert(5)
        bst2.insert(3)
        bst2.insert(7)
        bst2.insert(9)

        # Execution
        got = self.bst.is_same_tree(bst1.root, bst2.root)
        # Validation
        self.assertFalse(got)

    def test_find_two_sum_target(self):
        want1 = 8
        is_there = self.bst.find_two_sum_target(want1)
        self.assertTrue(is_there)

        want2 = 22
        is_there = self.bst.find_two_sum_target(want2)
        self.assertFalse(is_there)

    def test_merge_two_binary_trees(self):
        bst1 = main.BinarySearchTree()
        bst1.insert(6)
        bst1.insert(2)
        bst1.insert(7)
        bst1.insert(5)

        bst2 = main.BinarySearchTree()
        bst2.insert(2)
        bst2.insert(4)
        bst2.insert(9)
        bst2.insert(0)
        bst2.insert(1)

        root = self.bst.merge_two_binary_trees(bst1.root, bst2.root)

        self.assertEqual(root.value, 8)
        self.assertEqual(root.left.value, 2)
        self.assertEqual(root.left.right.value, 6)
        self.assertEqual(root.right.value, 11)
        self.assertEqual(root.right.right.value, 9)

    def test_get_all_nodes_value(self):
        want = [3, 6, 5, 7, 1, 10]
        got = self.bst.get_all_nodes_value()

        self.assertEqual(set(want), set(got))

    def test_get_minimum_abs_diff(self):
        numbers = self.bst.get_all_nodes_value()
        got = self.bst.minimum_abs_diff(numbers)

        self.assertEqual(1, got)  # 6と5の絶対値差の１

    def test_find_tilt(self):
        want = 49
        got = self.bst.find_tilt()

        self.assertEqual(want, got)

    def test_level_order(self):
        want = [[3], [1, 6], [5, 7], [10]]
        got = self.bst.level_order()

        self.assertEqual(want, got)

    def test_sum_of_all_nodes_value(self):
        want = 32
        got = self.bst.sum_of_all_nodes_value()

        self.assertEqual(want, got)

    def test_sum_of_right_leaves(self):
        want = 10
        got = self.bst.sum_of_right_leaves()

        self.assertEqual(want, got)

    def test_sum_of_left_leaves(self):
        want = 6
        got = self.bst.sum_of_left_leaves()

        self.assertEqual(want, got)

    def test_sum_of_left_leaves_stack(self):
        want = 6
        got = self.bst.sum_of_left_leaves_stack()

        self.assertEqual(want, got)

    def test_sum_of_left_leaves_queue(self):
        want = 6
        got = self.bst.sum_of_left_leaves_queue()

        self.assertEqual(want, got)

    def test_find_all_tree_paths(self):
        god = self.bst.find_all_tree_paths()
        want = [[3, 1], [3, 6, 5], [3, 6, 7, 10]]

        self.assertEqual(god, want)

    def test_path_sum(self):
        is_there = self.bst.path_sum(26)
        self.assertTrue(is_there)

    def test_all_specific_sum(self):
        # Init
        self.bst.insert(9)
        self.bst.insert(8)
        self.bst.insert(17)

        # Execution
        want = [[3, 6, 7, 10, 9, 8], [3, 6, 7, 10, 17]]
        got = self.bst.specific_tree_paths(43)

        self.assertEqual(want, got)

    def test_max_depth(self):
        depth = self.bst.max_depth()
        self.assertEqual(depth, 4)

    def test_invert_tree(self):
        self.bst.invert_tree()

        self.assertEqual(3, self.bst.root.value)
        self.assertEqual(1, self.bst.root.right.value)
        self.assertEqual(6, self.bst.root.left.value)
        self.assertEqual(7, self.bst.root.left.left.value)
        self.assertEqual(5, self.bst.root.left.right.value)
        self.assertEqual(10, self.bst.root.left.left.left.value)

    def test_invert_tree_stack(self):
        self.bst.invert_tree_stack()

        self.assertEqual(3, self.bst.root.value)
        self.assertEqual(1, self.bst.root.right.value)
        self.assertEqual(6, self.bst.root.left.value)
        self.assertEqual(7, self.bst.root.left.left.value)
        self.assertEqual(5, self.bst.root.left.right.value)
        self.assertEqual(10, self.bst.root.left.left.left.value)

    def test_invert_queue(self):
        self.bst.invert_tree_queue()

        self.assertEqual(3, self.bst.root.value)
        self.assertEqual(1, self.bst.root.right.value)
        self.assertEqual(6, self.bst.root.left.value)
        self.assertEqual(7, self.bst.root.left.left.value)
        self.assertEqual(5, self.bst.root.left.right.value)
        self.assertEqual(10, self.bst.root.left.left.left.value)

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

    def test_preorder_generate(self):
        want = [3, 1, 6, 5, 7, 10]

        got = []
        for data in self.bst.preorder_generate(self.bst.root):
            got.append(data)

        self.assertEqual(want, got)

    def test_post_order_generate(self):
        want = [10, 7, 5, 6, 1, 3]

        got = []
        for data in self.bst.postorder_generate(self.bst.root):
            got.append(data)
        self.assertEqual(want, got)

    def test_inorder_generate(self):
        nodes = self.bst.inorder_generate(self.bst.root)
        self.assertEqual(nodes.__next__(), 1)
        self.assertEqual(nodes.__next__(), 3)
        self.assertEqual(nodes.__next__(), 5)
        self.assertEqual(nodes.__next__(), 6)
        self.assertEqual(nodes.__next__(), 7)
        self.assertEqual(nodes.__next__(), 10)


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
    pytest.main()
