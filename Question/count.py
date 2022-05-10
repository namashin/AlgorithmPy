from collections import Counter
from typing import Tuple, List
import operator


"""
Count most appear str in the sentence.
input = 'hello world, to all people in this world.'

>>> ('l', 7)
"""


def count_words_no1(chars: str) -> Tuple[str, int]:
    chars = chars.lower()

    cache = []
    for char in chars:
        if not char.isspace():
            cache.append((char, chars.count(char)))

    # l = [(char, chars.count(char)) for char in chars if not char.isspace()]

    # return max(cache, key=lambda x: x[1])
    return max(cache, key=operator.itemgetter(1))


def count_words_no2(chars: str) -> Tuple[str, int]:
    chars = chars.lower()
    cache = {}  # dict

    for char in chars:
        if not char.isspace():
            cache[char] = cache.get(char, 0) + 1
            # value = cache.get(second)　について
            # getメソッドは指定されたキーがdictにあれば値を返し、なければデフォルトでNone、指定されていれば第2引数の値を返します。

    max_key = max(cache, key=cache.get)
    # 一番多く出現する文字keyがわかれば、そのvalueもdictから取ってこれる
    return max_key, cache[max_key]


def count_words_no3(chars: str) -> Tuple[str, int]:
    chars = chars.lower()

    d = Counter()
    for char in chars:
        if not char.isspace():
            d[char] += 1

    # これでもいい
    # counter = Counter(char)
    # return counter.most_common(1)

    max_key = max(d, key=d.get)
    return max_key, d[max_key]


"""
x = [1, 2, 3, 4, 4, 5, 5, 6, 6, 10]
y = [2, 4, 6, 7, 8, 10, 10, 10]

これが

x = [1, 2, 3, 4, 4, 5, 5, 6, 6]
y = [2, 7, 8, 10, 10, 10]

"""


def min_count_remove_no1(x: List[int], y: List[int]) -> None:
    count_x = {}
    count_y = {}

    for i in x:
        count_x[i] = count_x.get(i, 0) + 1

    for i in y:
        count_y[i] = count_y.get(i, 0) + 1

    for x_key, x_value in count_x.items():
        y_value = count_y.get(x_key)
        if y_value:
            if y_value > x_value:
                x[:] = [i for i in x if i != x_key]
            elif x_value > y_value:
                y[:] = [i for i in y if i != x_key]
            # elif y_value == x_value:
            #     """数一緒ならそのまま"""
            #     continue


def min_count_remove_no2(x: List[int], y: List[int]) -> None:
    """Counter()はdictのように使える"""
    count_x = Counter(x)
    count_y = Counter(y)

    for x_key, x_value in count_x.items():
        y_value = count_y.get(x_key)
        if y_value:
            """y_valueが存在する時"""
            if x_value < y_value:
                x[:] = [i for i in x if i != x_key]
                # これをリスト内表記化させた。
                # x = []
                # for i in x:
                #     if i != x_key:
                #         x.append(i)

            elif x_value > y_value:
                y[:] = [i for i in y if i != x_key]
            elif x_value == y_value:
                continue
