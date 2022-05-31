from typing import List, Tuple


def find_symmetric(pairs: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    cache = {}

    for pair in pairs:
        first, second = pair[0], pair[1]

        value = cache.get(second, None)
        if value is None:
            cache[first] = second

        else:
            value == first:
                yield pair


if __name__ == '__main__':
    """
    find symmetric:
    input = [(1, 2), (3, 5), (5, 3), (7, 4), (4, 7), (8, 1), (5, 7)]
    answer: (3, 5), (7, 4)
    """
    input = [(1, 2), (3, 5), (5, 3), (7, 4), (4, 7), (8, 1), (5, 7)]
    for pair in find_symmetric(input):
        print(pair)
    
