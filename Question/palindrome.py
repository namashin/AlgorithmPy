from typing import List, Generator


def is_palindrome(chars: str) -> bool:
    len_chars = len(chars)

    if not len_chars:
        return False

    if len_chars == 1:
        return True

    left, right = 0, len_chars - 1
    while left < right:
        if chars[left] != chars[right]:
            return False

        left += 1
        right -= 1

    return True


# 内側から見ていくパターン
def find_palindrome(chars: str, left: int, right: int) -> List[str]:
    result = []
    while 0 <= left and right <= len(chars) - 1:
        if chars[left] != chars[right]:
            break

        result.append(chars[left: right + 1])
        left -= 1
        right += 1

    return result


# 回文かどうか内側から見ていくパターン
def find_palindrome_v2(chars: str, left: int, right: int) -> Generator:
    while 0 <= left and right <= len(chars) - 1:
        if chars[left] != chars[right]:
            break

        yield chars[left: right + 1]

        left -= 1
        right += 1


def find_all_palindrome(chars: str):
    result = []
    len_chars = len(chars)

    if not len_chars:
        return result

    if len_chars == 1:
        result.append(chars)

    # aba 奇数パターン
    # abba 偶数パターン
    for i in range(1, len_chars - 1):
        [result.append(s) for s in find_palindrome(chars, i - 1, i + 1)]
        [result.append(s) for s in find_palindrome(chars, i, i + 1)]

    return result


def find_all_palindrome_v2(chars: str) -> Generator:
    len_chars = len(chars)

    if not len_chars:
        yield

    if len_chars == 1:
        yield chars

    # aba 奇数パターン
    # abba 偶数パターン
    for i in range(1, len_chars - 1):
        yield from find_palindrome_v2(chars, i - 1, i + 1)
        yield from find_palindrome_v2(chars, i, i + 1)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = self.find_all_palindrome(s)
        print(result)
        answer = ""
        for palindrome in result:
            if len(answer) < len(palindrome):
                answer = palindrome

        return answer

    def find_palindrome(self, chars: str, left: int, right: int):
        result = []
        while 0 <= left and right <= len(chars) - 1:
            if chars[left] != chars[right]:
                break

            result.append(chars[left: right + 1])
            left -= 1
            right += 1

        return result

    def find_all_palindrome(self, chars: str):
        result = []
        len_chars = len(chars)

        if not len_chars:
            return result

        if len_chars == 1:
            result.append(chars)

        if len(chars) == 2:
            [result.append(s) for s in self.find_palindrome(chars, 0, 1)]

        for i in range(len_chars):
            [result.append(s) for s in self.find_palindrome(chars, i, i)]
            [result.append(s) for s in self.find_palindrome(chars, i, i + 1)]

        return result


if __name__ == '__main__':
    # Palindrome 作成
    text = 'aba'
    text = 'aba'
    text = 'racecar'
    # 方法１
    print(text == text[::-1])

    # 方法２
    print(text == ''.join(reversed(text)))
