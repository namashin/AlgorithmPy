import math
from typing import List


def is_prime(number: int) -> bool:
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def is_prime_v2(number: int) -> bool:
    if number <= 1:
        return False

    for i in range(2, math.floor(math.sqrt(number) + 1)):
        if number % i == 0:
            return False

    return True


def is_prime_v3(number: int) -> bool:
    if number <= 1:
        return False

    i = 2
    while i < number:
        if number % i == 0:
            return False

        i += 1

    return True


def is_prime_v4(number: int) -> bool:
    if number <= 1:
        return False

    if number % 2 == 0 and number % 3 == 0:
        return False

    for i in range(5, math.floor(math.sqrt(number + 1)), 6):
        if number % i == 0:
            return False

    return True


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


if __name__ == '__main__':
    # 素数判定
    print(is_prime(30))
    print(is_prime_v2(30))
    print(is_prime_v3(30))
    print(is_prime_v4(30))
