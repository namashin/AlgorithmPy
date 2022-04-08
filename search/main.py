from typing import List, NewType

Index = NewType("index", int)


# 既にソートされ終わった事を想定
# その後、目的の数字のインデックスを取得
def binary_search(numbers: List[int], target: int) -> Index:
    left, right = 0, len(numbers) - 1

    while left <= right:

        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid

        elif numbers[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


def binary_search_recursive(numbers: List[int], target: int) -> Index:
    def _binary_search_recursive(numbers: List[int], target: int, left: int, right: int) -> Index:

        if left > right:
            return -1

        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid

        elif numbers[mid] < target:
            return _binary_search_recursive(numbers, target, mid + 1, right)

        else:
            return _binary_search_recursive(numbers, target, left, mid - 1)

    return _binary_search_recursive(numbers, target, 0, len(numbers) - 1)
