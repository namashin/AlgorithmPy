import string


def snake_print(numbers: str) -> None:
    result = [[], [], []]
    result_indexes = {0, 1, 2}
    insert_index = 1

    for i, number in enumerate(numbers):
        if i % 4 == 1:
            insert_index = 0
        elif i % 2 == 0:
            insert_index = 1
        elif i % 4 == 3:
            insert_index = 2

        result[insert_index].append(number)
        for rest_index in result_indexes - {insert_index}:
            result[rest_index].append(' ')

    for line in result:
        print(''.join(line))


def snake_print2(chars: str, depth: int):
    result = [[] for _ in range(depth)]
    result_indexes = {i for i in range(depth)}
    insert_index = int(depth / 2)

    def pos(i): return i + 1
    def neg(i): return i - 1
    # pos = lambda i: i + 1
    # neg = lambda i: i - 1

    op = neg

    for char in chars:
        result[insert_index].append(char)
        for rest_indexes in result_indexes - {insert_index}:
            result[rest_indexes].append(' ')

        if insert_index == 0:
            op = pos
        if depth - 1 == insert_index:
            op = neg

        insert_index = op(insert_index)

    for line in result:
        print(''.join(line))


if __name__ == '__main__':
    nums = [str(i) for _ in range(3) for i in range(0, 10)]
    nums = ''.join(nums)
    snake_print(nums)

    print("##########################################")

    alpha = [s for _ in range(2) for s in string.ascii_lowercase]
    strings = ''.join(alpha)
    snake_print2(strings, depth=5)
