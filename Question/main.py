import operator
from typing import List, Tuple
from collections import Counter


"""
find symmetric:
input = [(1, 2), (3, 5), (5, 3), (7, 4), (4, 7), (8, 1), (5, 7)]
answer: (3, 5), (7, 4)
"""


def find_symmetric(pairs: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    cache = {} 

    for pair in pairs:
        first, second = pair[0], pair[1]

        value = cache.get(second)
        if value is None:
            cache[first] = second

        if value == first:
            yield pair

            
# value = cache.get(second)　について           
# getメソッドは指定されたキーがdictにあれば値を返し、なければデフォルトでNone、指定されていれば第2引数の値を返します。            


"""
Count most appear str in the sentence.
input = 'hello world, to all people in this world.
answer: 
"""


def count_words_no1(chars: str) -> Tuple[str, int]:
    chars = chars.lower()

    cache = []  # list
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


"""
[1] => [2] => 2
[2, 3] => [2, 4] => 24
[9, 9] => [1, 0, 0] => 100
[7, 8, 9] => [7, 9, 0] => 790
[0, 0, 0, 9, 9, 9, 9] => [1, 0, 0, 0, 0] => 10000
"""

# l = [1, 2, 3]
# l = int(''.join([str(i) for i in l]))
# >>> 123


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
    else:
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

    return list_to_int_plus1_part1(numbers)


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


"""
キャッシュデコレーターの生成
"""


def memoize(f):
    cache = dict()

    def _wrapper(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return _wrapper


@memoize
def cpu_bound(num: int) -> int:
    x = 0
    for i in range(100000):
        x += num * i
    return x


# json形式を検証する関数
def validate_json(chars: str) -> bool:
    lookup = {'{': '}', '(': ')', '[': ']'}
    stack = []

    for char in chars:
        if char in lookup.keys():
            stack.append(lookup[char])

        elif char in lookup.values():
            # pythonのlistは、空であればFalse、中身が入ってればTrueを返す性質があります。
            if stack is None:
                return False

            if char != stack.pop():
                return False

    if stack:
        """最終的にstackの中は空リスト: [] じゃないといけない"""
        return False

    return True


# list_in_list = [1, 4, 6, [2, 4], [3, 4, [7, 3, 2], 3], 9]
# リストの中のリストを全て平らに
def flatten(list_in_list):
    for i in list_in_list:
        if isinstance(i, list):
            yield from flatten(i)
        else:
            yield i


# 全ての順列を表示させる
# from itertools import permutations
#
# for r in permutations([1, 2, 3]):
#     print(r)
#
# これと同じ関数を自作

def all_perms_v1(elements: List[int]) -> List[List[int]]:
    result = []

    if len(elements) <= 1:
        return [elements]

    for perms in all_perms_v1(elements[1:]):
        for i in range(len(elements)):
            result.append(perms[:i] + elements[0:1] + perms[i:])

    return result


def all_perms_v2(elements: List[int]) -> List[List[int]]:
    if len(elements) <= 1:
        yield elements

    for perms in all_perms_v1(elements[1:]):
        for i in range(len(elements)):
            yield perms[:i] + elements[0:1] + perms[i:]


# 与えられた数字が含む全ての素数を表示
def generate_primes_v1(number: int) -> List[int]:
    primes = []
    for x in range(2, number + 1):
        for y in range(2, x):
            if x % y == 0:
                break
        else:
            primes.append(x)

    return primes


def generate_primes_v2(number: int) -> List[int]:
    primes = []
    cache = {}

    for x in range(2, number + 1):
        is_prime = cache.get(x)
        if is_prime is False:
            continue

        primes.append(x)
        cache[x] = True
        for y in range(x*2, number + 1, x):
            cache[y] = False

    return primes


# yield 使用
def generate_primes_v3(number: int) -> List[int]:
    cache = {}

    for x in range(2, number + 1):
        is_prime = cache.get(x)
        if is_prime is False:
            continue

        yield x
        cache[x] = True
        for y in range(x*2, number + 1, x):
            cache[y] = False


# Palindrome 作成
# text = 'aba' # => True
# text = 'aba' # => False
# text = 'racecar'  # => True
# 方法１
# print(text == text[::-1])
#
# 方法２
# print(text == ''.join(reversed(text)))


def is_palindrome(check_text: str) -> bool:
    len_text = len(check_text)
    if not len_text:
        return False

    if len_text == 1:
        return True

    start = 0
    end = len_text - 1
    while start < end:
        if check_text[start] != check_text[end]:
            return False

        start += 1
        end -= 1

    return True
