import collections
from typing import Optional, List
import sys
from collections import deque


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

        self.all_nodes = []

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

    def find_two_sum_target(self, target_number: int) -> bool:
        elements = []

        def get_all_elements(node: Node) -> None:
            nonlocal elements

            if node is None:
                return

            elements.append(node.value)

            get_all_elements(node.left)
            get_all_elements(node.right)

        get_all_elements(self.root)

        for i, value1 in enumerate(elements):
            for value2 in elements[i:]:
                if (value1 + value2) == target_number:
                    return True

        return False

    def merge_two_binary_trees(self, root1: Node, root2: Node) -> Node:
        if root1 and root2:
            node = Node(root1.value + root2.value)

            node.left = self.merge_two_binary_trees(root1.left, root2.left)
            node.right = self.merge_two_binary_trees(root1.right, root2.right)
            return node

        else:
            return root1 or root2

    def get_all_nodes_value(self) -> List[int]:
        all_nodes = []

        def _get_all_nodes_value(node: Node) -> Optional[List[int]]:
            nonlocal all_nodes

            if not node:
                return

            all_nodes.append(node.value)

            _get_all_nodes_value(node.left)
            _get_all_nodes_value(node.right)

        _get_all_nodes_value(self.root)

        return all_nodes

    def minimum_abs_diff(self, numbers: List[int]) -> int:
        import sys
        minimum_abs = sys.maxsize

        len_numbers = len(numbers)
        for i in range(len_numbers):
            for j in range(i + 1, len_numbers):
                abs_data = abs(numbers[i] - numbers[j])
                minimum_abs = min(abs_data, minimum_abs)

        return minimum_abs

    def find_tilt(self) -> int:
        """
        :return: 各ノードのチルドレンの絶対値の和
        """
        total_tilt = 0

        def _find_tilt(node: Node) -> int:
            # nonlocal 文は、関数のひとつ外側の変数を参照します。
            nonlocal total_tilt

            if not node:
                return 0

            left = _find_tilt(node.left)
            right = _find_tilt(node.right)
            tilt = abs(left - right)
            total_tilt += tilt

            return left + right + node.value

        _find_tilt(self.root)
        return total_tilt

    def sum_of_all_nodes_value(self):
        def _sum_of_all_nodes_value(node: Node) -> int:
            if not node:
                return 0

            left = _sum_of_all_nodes_value(node.left)
            right = _sum_of_all_nodes_value(node.right)

            return left + right + node.value

        return _sum_of_all_nodes_value(self.root)

    def sum_of_right_leaves(self) -> Optional[int]:
        total = 0

        def _sum_of_right_leaves(node: Node) -> Optional[int]:
            nonlocal total

            if not node:
                return

            if node.right and (not node.right.right) and (not node.right.left):
                total += node.right.value

            _sum_of_right_leaves(node.left)
            _sum_of_right_leaves(node.right)

        _sum_of_right_leaves(self.root)

        return total

    def sum_of_left_leaves(self) -> Optional[int]:
        total = 0

        def _sum_of_left_leaves(node: Node):
            nonlocal total

            if not node:
                return

            if node.left and (not node.left.left) and (not node.left.right):
                total += node.left.value

            _sum_of_left_leaves(node.left)
            _sum_of_left_leaves(node.right)

        _sum_of_left_leaves(self.root)
        return total

    def sum_of_left_leaves_stack(self) -> int:
        original_root = self.root

        stack = [original_root]
        total = 0

        while stack:
            root = stack.pop()

            if root.left and (not root.left.left) and (not root.left.right):
                total += root.left.value

            if root.left:
                stack.append(root.left)

            if root.right:
                stack.append(root.right)

        return total

    def sum_of_left_leaves_queue(self):
        original_root = self.root
        queue = deque([original_root])
        total = 0

        while queue:
            root = queue.popleft()

            if root.left and (not root.left.left) and (not root.left.right):
                total += root.left.value

            if root.left:
                queue.append(root.left)

            if root.right:
                queue.append(root.right)

        return total

    def path_sum(self, target_sum: int) -> bool:
        def _path_sum(root: Node, _target_sum: int) -> bool:
            if not root:
                return False

            if (not root.left) and (not root.right) and (root.value == _target_sum):
                return True

            _target_sum -= root.value

            return _path_sum(root.left, _target_sum) or _path_sum(root.right, _target_sum)

        return _path_sum(self.root, target_sum)

    def specific_tree_paths(self, target_sum: int) -> List[List[int]]:
        def _specific_tree_paths(root: Node, _target_sum: int) -> List[List[int]]:
            if not root:
                return []

            if (not root.left) and (not root.right) and _target_sum == root.value:
                return [[root.value]]

            temp = _specific_tree_paths(root.left, _target_sum - root.value) \
                   + _specific_tree_paths(root.right, _target_sum - root.value)

            return [[root.value] + i for i in temp]

        return _specific_tree_paths(self.root, target_sum)

    def find_all_tree_paths(self):
        def _find_all_tree_paths(root: Node) -> List[List[int]]:
            if not root:
                return []

            if (not root.left) and (not root.right):
                return [[root.value]]

            temp = _find_all_tree_paths(root.left) + _find_all_tree_paths(root.right)

            return [[root.value] + i for i in temp]

        return _find_all_tree_paths(self.root)

    def invert_tree(self):
        def _invert_tree(root: Node) -> Node:
            if root:
                root.left, root.right = _invert_tree(root.right), _invert_tree(root.left)
                return root

        _invert_tree(self.root)

    def invert_tree_stack(self):
        def _invert_tree_stack(root: Node) -> None:
            stack = [root]

            while stack:
                node = stack.pop()
                if node:
                    node.left, node.right = node.right, node.left
                    stack.append(node.left)
                    stack.append(node.right)

        _invert_tree_stack(self.root)

    def invert_tree_queue(self):
        def _invert_tree_queue(root: Node):
            queue = collections.deque([root])

            while queue:
                node = queue.popleft()

                if node:
                    node.left, node.right = node.right, node.left
                    queue.append(node.left)
                    queue.append(node.right)

        _invert_tree_queue(self.root)

    def max_depth(self) -> Optional[int]:
        if self.root is None:
            return

        def _max_depth(root: Optional[Node]) -> int:
            if not root:
                return 0

            left = _max_depth(root.left)
            right = _max_depth(root.right)
            return max(left, right) + 1
            # return max(_max_depth(node.left), _max_depth(node.right)) + 1
            # でもいい

        return _max_depth(self.root)

    def size_recursive(self) -> Optional[int]:
        def _size(node: Node) -> int:
            if node is None:
                return 0
            return _size(node.left) + _size(node.right) + 1

        return _size(self.root)

    def inorder(self):
        def _inorder(node: Node):
            if node:
                _inorder(node.left)
                print(node.value)
                _inorder(node.right)
        _inorder(self.root)

    def inorder_generate(self, root: Node):
        if root:
            yield from self.inorder_generate(root.left)
            yield root.value
            yield from self.inorder_generate(root.right)

    def preorder_generate(self, root):
        if root:
            yield root.value
            yield from self.preorder_generate(root.left)
            yield from self.preorder_generate(root.right)

    def postorder_generate(self, root: Node):
        if root:
            yield from self.postorder_generate(root.right)
            yield from self.postorder_generate(root.left)
            yield root.value

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

    def level_order(self) -> List[List[int]]:
        current = self.root

        if current is None:
            return []

        queue, result = deque([current]), []

        while queue:
            current_layer, size = [], len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

                current_layer.append(node.value)

            result.append(current_layer)

        return result

    def is_same_tree(self, node_1: Node, node_2: Node) -> bool:
        # 両方ともNoneのパターン
        if (not node_1) and (not node_2):
            return True

        # 両方ともNoneではないが、片方がNoneのパターン
        if (not node_1) or (not node_2):
            return False

        # 値違うパターン
        if node_1.value != node_2.value:
            return False

        # 両方ともTrue返ってきたら、True. 一方がFalseあるとFalse.
        return self.is_same_tree(node_1.right, node_2.right) and self.is_same_tree(node_1.left, node_2.left)

    def sum_root_to_leaf(self) -> int:
        sums = self.find_all_tree_paths()

        total = 0
        for path in sums:
            path = [str(integer) for integer in path]
            str_path = ''.join(path)
            total += int(str_path)

        return total


class MiniHeap(object):
    """
    heap の実装

    import heapq
    a = [7, 5, 3, 2, 4, 8, 10, 1]
    heapq.heapify(a)
    heapq.heappush(a, 6)
    heapq.heappop(a)
    print(a)
    """
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
