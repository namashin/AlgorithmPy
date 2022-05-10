
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
            if stack is None:
                return False

            if char != stack.pop():
                return False

    if stack:
        """
        最終的にstackの中は空リスト: [] じゃないといけない
        Pythonのlistは、空であればFalse、中身が入ってればTrueを返す性質があります。
        """
        return False

    return True


# list_in_list = [1, 4, 6, [2, 4], [3, 4, [7, 3, 2], 3], 9]
# >>> [1, 4, 6, 2, 4, 3, 4, 7, 3, 2, 3, 9]
# リストの中のリストを全て平らに
def flatten(list_in_list):
    for i in list_in_list:
        if isinstance(i, list):
            yield from flatten(i)
        else:
            yield i
