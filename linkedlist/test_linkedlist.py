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


class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.doubly_linked_list = main.DoublyLinkedList()
        self.doubly_linked_list.append(1)
        self.doubly_linked_list.append(2)
        self.doubly_linked_list.append(3)

    def tearDown(self) -> None:
        pass

    def test_append(self):
        self.assertEqual(1, self.doubly_linked_list.head.data)
        self.assertEqual(2, self.doubly_linked_list.head.next.data)
        self.assertEqual(3, self.doubly_linked_list.head.next.next.data)

        self.assertEqual(2, self.doubly_linked_list.head.next.next.prev.data)
        self.assertEqual(1, self.doubly_linked_list.head.next.next.prev.prev.data)

    def test_insert(self):
        self.doubly_linked_list.insert(5)

        self.assertEqual(5, self.doubly_linked_list.head.data)

    def test_remove(self):
        self.doubly_linked_list.remove(2)

        self.assertEqual(1, self.doubly_linked_list.head.data)
        self.assertEqual(3, self.doubly_linked_list.head.next.data)

    def test_reverse_iterative(self):
        self.doubly_linked_list.reverse_iterative()

        self.assertEqual(3, self.doubly_linked_list.head.data)
        self.assertEqual(2, self.doubly_linked_list.head.next.data)
        self.assertEqual(1, self.doubly_linked_list.head.next.next.data)

    def test_reverse_recursive(self):
        self.doubly_linked_list.reverse_recursive()

        self.assertEqual(3, self.doubly_linked_list.head.data)
        self.assertEqual(2, self.doubly_linked_list.head.next.data)
        self.assertEqual(1, self.doubly_linked_list.head.next.next.data)


if __name__ == '__main__':
    unittest.main()
