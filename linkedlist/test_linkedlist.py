import unittest
import main


class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.linked_list = main.LinkedList()

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

    def test_remove_element(self):
        self.linked_list.append("Test1")
        self.linked_list.append("Test2")

        self.linked_list.remove_element("Test1")
        self.assertEqual("Test2", self.linked_list.head.data)

    def test_remove_elements(self):
        # Init
        self.linked_list.append("Test4")
        self.linked_list.append("Test1")
        self.linked_list.append("Test4")
        self.linked_list.append("Test2")
        self.linked_list.append("Test3")
        self.linked_list.append("Test4")
        self.linked_list.append("Test4")
        self.linked_list.append("Test4")
        self.linked_list.append("Test4")

        self.linked_list.append("Test5")

        # Execution
        self.linked_list.remove_elements("Test4")

        # Test
        self.assertEqual("Test1", self.linked_list.head.data)
        self.assertEqual("Test2", self.linked_list.head.next.data)
        self.assertEqual("Test3", self.linked_list.head.next.next.data)
        self.assertEqual("Test5", self.linked_list.head.next.next.next.data)

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

    def test_sort(self) -> None:
        self.linked_list.append(4)
        self.linked_list.append(2)
        self.linked_list.append(7)
        self.linked_list.append(5)

        self.linked_list.sort()

        self.assertEqual(2, self.linked_list.head.data)
        self.assertEqual(4, self.linked_list.head.next.data)
        self.assertEqual(5, self.linked_list.head.next.next.data)
        self.assertEqual(7, self.linked_list.head.next.next.next.data)

    def test_merge_two_linklist(self):
        # Init
        linklist_1 = main.LinkedList()
        linklist_1.append(2)
        linklist_1.append(4)
        linklist_1.append(5)
        linklist_1.append(9)
        linklist_1.append(10)

        linklist_2 = main.LinkedList()
        linklist_2.append(1)
        linklist_2.append(3)
        linklist_2.append(4)
        linklist_2.append(9)
        linklist_2.append(12)

        # Execution
        merged_node = self.linked_list.merge_two_linklist(linklist_1.head, linklist_2.head)

        # Validation
        self.assertEqual(1, merged_node.data)
        self.assertEqual(2, merged_node.next.data)
        self.assertEqual(3, merged_node.next.next.data)
        self.assertEqual(4, merged_node.next.next.next.data)
        self.assertEqual(4, merged_node.next.next.next.next.data)
        self.assertEqual(5, merged_node.next.next.next.next.next.data)
        self.assertEqual(9, merged_node.next.next.next.next.next.next.data)
        self.assertEqual(9, merged_node.next.next.next.next.next.next.next.data)
        self.assertEqual(10, merged_node.next.next.next.next.next.next.next.next.data)
        self.assertEqual(12, merged_node.next.next.next.next.next.next.next.next.next.data)

    def test_remove_nth_node_from_head(self):
        # Init
        self.linked_list.append(4)
        self.linked_list.append(2)
        self.linked_list.append(7)
        self.linked_list.append(5)
        self.linked_list.append(4)

        # Execution
        self.linked_list.remove_nth_node_from_head(1)

        # Validation
        self.assertEqual(2, self.linked_list.head.data)
        self.assertEqual(7, self.linked_list.head.next.data)


class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.doubly_linked_list = main.DoublyLinkedList()
        self.doubly_linked_list.append(1)
        self.doubly_linked_list.append(2)
        self.doubly_linked_list.append(3)
        self.doubly_linked_list.append(4)
        self.doubly_linked_list.append(5)

    def tearDown(self) -> None:
        pass

    def test_append(self):
        self.assertEqual(1, self.doubly_linked_list.head.data)
        self.assertEqual(2, self.doubly_linked_list.head.next.data)
        self.assertEqual(3, self.doubly_linked_list.head.next.next.data)

    def test_insert(self):
        self.doubly_linked_list.insert(6)

        self.assertEqual(6, self.doubly_linked_list.head.data)

    def test_remove_element(self):
        # Init
        self.doubly_linked_list.append(3)

        # Execution
        self.doubly_linked_list.remove_element(3)

        # Validation
        self.assertEqual(1, self.doubly_linked_list.head.data)
        self.assertEqual(2, self.doubly_linked_list.head.next.data)
        self.assertEqual(4, self.doubly_linked_list.head.next.next.data)
        self.assertEqual(5, self.doubly_linked_list.head.next.next.next.data)

    def test_remove_elements(self):
        # Init
        self.doubly_linked_list.append(3)

        # Execution
        self.doubly_linked_list.remove_elements(3)

        # Test
        self.assertEqual(1, self.doubly_linked_list.head.data)
        self.assertEqual(2, self.doubly_linked_list.head.next.data)
        self.assertEqual(4, self.doubly_linked_list.head.next.next.data)
        self.assertEqual(5, self.doubly_linked_list.head.next.next.next.data)

    def test_reverse_iterative(self):
        self.doubly_linked_list.reverse_iterative()

        self.assertEqual(5, self.doubly_linked_list.head.data)
        self.assertEqual(4, self.doubly_linked_list.head.next.data)
        self.assertEqual(3, self.doubly_linked_list.head.next.next.data)

    def test_reverse_recursive(self):
        self.doubly_linked_list.reverse_recursive()

        self.assertEqual(5, self.doubly_linked_list.head.data)
        self.assertEqual(4, self.doubly_linked_list.head.next.data)
        self.assertEqual(3, self.doubly_linked_list.head.next.next.data)

    def test_sort(self):
        self.doubly_linked_list.append(0)
        self.doubly_linked_list.append(9)
        self.doubly_linked_list.sort()

        self.assertEqual(0, self.doubly_linked_list.head.data)
        self.assertEqual(1, self.doubly_linked_list.head.next.data)
        self.assertEqual(2, self.doubly_linked_list.head.next.next.data)
        self.assertEqual(3, self.doubly_linked_list.head.next.next.next.data)
        self.assertEqual(4, self.doubly_linked_list.head.next.next.next.next.data)

    def test_remove_nth_node_from_head(self):
        self.doubly_linked_list.remove_nth_node_from_head(2)
        self.assertEqual(3, self.doubly_linked_list.head.next.data)

    def test_size(self):
        got = self.doubly_linked_list.size()
        want = 5

        self.assertEqual(got, want)

    def test_merge_two_linklist(self):
        # Init
        linklist_1 = main.LinkedList()
        linklist_1.append(2)
        linklist_1.append(4)
        linklist_1.append(5)
        linklist_1.append(9)
        linklist_1.append(10)

        linklist_2 = main.LinkedList()
        linklist_2.append(1)
        linklist_2.append(3)
        linklist_2.append(4)
        linklist_2.append(9)
        linklist_2.append(12)

        # Execution
        merged_node = self.doubly_linked_list.merge_two_linklist(list1=linklist_1.head, list2=linklist_2.head)

        # Validation
        self.assertEqual(1, merged_node.data)
        self.assertEqual(2, merged_node.next.data)
        self.assertEqual(3, merged_node.next.next.data)
        self.assertEqual(4, merged_node.next.next.next.data)
        self.assertEqual(4, merged_node.next.next.next.next.data)
        self.assertEqual(5, merged_node.next.next.next.next.next.data)
        self.assertEqual(9, merged_node.next.next.next.next.next.next.data)
        self.assertEqual(9, merged_node.next.next.next.next.next.next.next.data)
        self.assertEqual(10, merged_node.next.next.next.next.next.next.next.next.data)
        self.assertEqual(12, merged_node.next.next.next.next.next.next.next.next.next.data)


if __name__ == '__main__':
    unittest.main()
