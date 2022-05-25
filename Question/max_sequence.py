
from typing import List


def get_max_sequence(numbers: List[int], op) -> int:
    result_sequence, sum_sequence = 0, 0
    for num in numbers:
        sum_sequence = op(num, sum_sequence + num)

        result_sequence = op(result_sequence, sum_sequence)

    return result_sequence


def find_max_circular_sequence_sum(numbers: List[int]) -> int:
    max_sequence_sum = get_max_sequence(numbers, op=max)
    max_wrap_sequence = sum(numbers) - get_max_sequence(numbers, op=min)

    return max(max_sequence_sum, max_wrap_sequence)


if __name__ == '__main__':
    input1 = [1, -1, 3, -5, 2]
    input2 = [-100, 3, 5, -4, 6, -2, -200]
    print(find_max_circular_sequence_sum(input2))