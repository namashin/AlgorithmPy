from typing import List

def snake(numbers: str):
    result = [[], [], []]
    result_indexes = {0, 1, 2}
    append_index = 1

    for i, num in enumerate(numbers):
        if i % 2 == 0:
            append_index = 1
        elif i % 4 == 1:
            append_index = 0
        elif i % 4 == 3:
            append_index = 2

        result[append_index].append(num)

        for rest_index in result_indexes - {append_index}:
            result[rest_index].append(' ')

    return result



if __name__ == '__main__':
    for line in snake('0123456789'):
        print(''.join(line))
