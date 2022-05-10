from typing import List


def delete_duplicate_v1(numbers: List[int]) -> List[int]:
    tmp = []

    for num in numbers:
        if num not in tmp:
            tmp.append(num)
    numbers[:] = tmp

    return numbers


def delete_duplicate_v2(numbers: List[int]) -> List[int]:
    i = len(numbers) - 1

    while 0 <= i:
        if numbers[i] == numbers[i - 1]:
            numbers.pop(i)

        i -= 1

    return numbers


if __name__ == '__main__':
    # すでにsortされている事を想定
    # 重複を削除

    l = [1, 3, 4, 4, 5, 5, 5, 6, 8, 9, 9, 9]
    print(list(set(l)))
    print([n for i, n in enumerate(l) if n not in l[:i]])
    print(delete_duplicate_v1(l))
