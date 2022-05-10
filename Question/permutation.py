from typing import List, Generator
from itertools import permutations


def all_perms(elements: List[int]) -> List[List[int]]:
    result = []

    if len(elements) <= 1:
        return [elements]

    for perms in all_perms(elements[1:]):
        for i in range(len(elements)):
            result.append(perms[:i] + elements[0:1] + perms[i:])

    return result


def all_perms_v2(elements: List[int]) -> Generator:
    if len(elements) <= 1:
        return [elements]

    for perms in all_perms(elements[1:]):
        for i in range(len(elements)):
            yield perms[:i] + elements[0:1] + perms[i:]


if __name__ == '__main__':
    # 全ての順列パターン表示

    for p in permutations([1, 2, 3]):
        print(p)
