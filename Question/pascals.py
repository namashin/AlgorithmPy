from typing import List


def pascal(depth: int) -> List[List[int]]:
    results = [[1] * (i + 1) for i in range(depth)]

    for line in range(2, depth):
        for i in range(1, line):
            results[line][i] = results[line - 1][i - 1] + results[line - 1][i]

    return results


def print_pascal(data: List[List[int]]) -> None:
    max_digit = len(str(max(data[-1])))
    width = max_digit + (max_digit % 2) + 2

    for i, line in enumerate(data):
        numbers = ''.join(str(i).center(width, ' ') for i in line)
        print((' ' * int(width / 2)) * (len(data) - i), numbers)

    #             1
    #           1   1
    #         1   2   1
    #       1   3   3   1
    #     1   4   6   4   1
    #   1   5   10  10  5   1
    # 1   6   15  20  15  6   1


if __name__ == '__main__':
    print_pascal(pascal(7))
