from typing import List


def order_list_by_index(chars: List[str], indexes: List[int]) -> str:
    i, len_indexes = 0, len(indexes)

    while i < len_indexes:
        while i != indexes[i]:
            index = indexes[i]

            chars[i], chars[index] = chars[index], chars[i]
            indexes[i], indexes[index] = indexes[index], indexes[i]

        i += 1

    return ''.join(chars)


def order_list_by_index_v2(chars: List[str], indexes: List[int]) -> str:
    tmp = [''] * len(chars)

    for i, index in enumerate(indexes):
        tmp[index] = chars[i]

    return ''.join(tmp)


def even_first_odd_last(numbers: List[int]) -> List[int]:
    evens = []
    odds = []

    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
        else:
            odds.append(number)

    numbers[:] = evens + odds

    return numbers


def even_first_odd_last_v2(numbers: List[int]) -> List[int]:
    left, right = 0, len(numbers) - 1

    while left < right:
        if numbers[left] % 2 == 0:
            left += 1
        else:
            numbers[left], numbers[right] = numbers[right], numbers[left]
            right -= 1

    return numbers


if __name__ == '__main__':
    # 指定のindex通りに並び替え
    python = ['y', 'n', 'p', 't', 'o', 'h']
    indexes = [1, 5, 0, 2, 4, 3]
    print(order_list_by_index(python, indexes))

    """
    偶数奇数並び替え
    偶数先、奇数後
    """
    from random import randint
    nums = [randint(0, 100) for _ in range(10)]
    print(even_first_odd_last(nums))
