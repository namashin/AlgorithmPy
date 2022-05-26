from typing import List


def bubble_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)

    for i in range(len_numbers):
        for j in range(len_numbers - 1 - i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


def selection_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)

    for i in range(len_numbers):
        min_index = i

        for j in range(i+1, len_numbers):
            if numbers[min_index] > numbers[j]:
                min_index = j
        numbers[min_index], numbers[i] = numbers[i], numbers[min_index]

    return numbers


def insertion_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)

    for i in range(1, len_numbers):
        temp = numbers[i]
        j = i - 1
        while j >= 0 and temp < numbers[j]:
            numbers[j+1] = numbers[j]
            j -= 1

        numbers[j+1] = temp

    return numbers


def quick_sort(numbers: List[int]) -> List[int]:
    def _quick_sort(_numbers: List[int], low: int, high: int) -> None:
        if low < high:
            partition_index = partition(_numbers, low, high)
            _quick_sort(_numbers, low, partition_index - 1)
            _quick_sort(_numbers, partition_index + 1, high)

    _quick_sort(numbers, low=0, high=len(numbers)-1)

    return numbers


def partition(numbers: List[int], low: int, high: int) -> int:
    i = low - 1
    pivot = numbers[high]
    for j in range(low, high):
        if numbers[j] <= pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]

    i += 1
    numbers[high], numbers[i] = numbers[i], numbers[high]
    return i
