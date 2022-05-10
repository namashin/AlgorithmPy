from typing import List


def list_to_int_plus1_part1(numbers: List[int]) -> int:
    # リストの一番後ろのインデックス取得 (i)
    i = len(numbers) - 1
    numbers[i] += 1

    while i > 0:
        if numbers[i] != 10:
            remove_zero(numbers)
            break

        # numbers[i] が 10の時
        numbers[i] = 0
        numbers[i - 1] += 1

        i -= 1

    """リストの先頭が10だった場合の処理"""
    if numbers[0] == 10:
        numbers[0] = 1
        numbers.append(0)

    return list_to_int(numbers)


def list_to_int_plus1_part2(numbers: List[int]) -> int:
    i = len(numbers) - 1
    numbers[i] += 1

    while 0 < i:
        if numbers[i] != 10:
            remove_zero(numbers)
            break

        elif numbers[i] == 10:
            numbers[i] = 0
            numbers[i-1] += 1

        i -= 1

    return list_to_int(numbers)


def remove_zero(numbers: List[int]) -> None:
    if numbers and numbers[0] == 0:
        numbers.pop(0)
        remove_zero(numbers)


def list_to_int(numbers: List[int]) -> int:
    """
    ex:
    [1, 2, 4] を 124 としたい

    reversedして[4, 2, 1]
    4 * (10 ** 0) + 2 * (10 ** 1) + 1 * (10 ** 2)
    4 + 20 + 100

    = 124
    """
    sum_numbers_of_list = 0
    for i, num in enumerate(reversed(numbers)):
        sum_numbers_of_list += num * (10 ** i)
    return sum_numbers_of_list


if __name__ == '__main__':
    """
    [1] => [2] => 2
    [2, 3] => [2, 4] => 24
    [9, 9] => [1, 0, 0] => 100
    [7, 8, 9] => [7, 9, 0] => 790
    [0, 0, 0, 9, 9, 9, 9] => [1, 0, 0, 0, 0] => 10000
    """

    l = [1, 2, 3]
    l = int(''.join([str(i) for i in l]))
