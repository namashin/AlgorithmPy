import unittest
import main


class TestStack(unittest.TestCase):

    def setUp(self) -> None:
        self.stack = main.Stack()

    def tearDown(self) -> None:
        pass

    def test_push(self):
        self.stack.push("No1")
        self.stack.push("No2")
        self.stack.push("No3")

        self.assertEqual("No1", self.stack.stack[0])
        self.assertEqual("No3", self.stack.stack[2])

    def test_pop(self):
        self.stack.push("No1")
        self.stack.push("No2")
        self.stack.push("No3")

        value = self.stack.pop()

        self.assertEqual(value, "No3")


class TestQueue(unittest.TestCase):

    def setUp(self) -> None:
        self.queue = main.Queue()

    def tearDown(self) -> None:
        pass

    def test_push(self):
        self.queue.push("No1")
        self.queue.push("No2")
        self.queue.push("No3")

        self.assertEqual("No1", self.queue.queue[0])
        self.assertEqual("No3", self.queue.queue[2])

    def test_pop(self):
        self.queue.push("No1")
        self.queue.push("No2")
        self.queue.push("No3")

        value = self.queue.pop()

        self.assertEqual(value, "No1")
        self.assertEqual(2, len(self.queue.queue))


if __name__ == '__main__':
    unittest.main()
