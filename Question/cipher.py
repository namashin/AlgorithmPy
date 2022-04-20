import string
from typing import Generator, Tuple


def caesar_cipher_1(clear_text: str, shift: int) -> str:
    result = ''

    for char in clear_text:
        if char.isupper():
            alphabet = string.ascii_uppercase
        elif char.islower():
            alphabet = string.ascii_lowercase
        else:
            result += char
            continue

        shifted_index = (alphabet.index(char) + shift) % len(alphabet)
        result += alphabet[shifted_index]

    return result


def caesar_cipher_2(clear_text: str, shift: int) -> str:
    result = ''
    len_alphabet = ord('Z') - ord('A') + 1

    for char in clear_text:
        if char.isupper():
            result += chr((ord(char) + shift - ord('A')) % len_alphabet + ord('A'))
        elif char.islower():
            result += chr((ord(char) + shift - ord('a')) % len_alphabet + ord('a'))
        else:
            result += char

    return result


def caesar_cipher_hacking(clear_text: str) -> Generator[Tuple[int, str], None, None]:
    len_alphabet = len(string.ascii_uppercase)

    for candidate_shift in range(1, len_alphabet + 1):
        result = ''
        for char in clear_text:
            if char.isupper():
                alphabet = string.ascii_uppercase
            elif char.islower():
                alphabet = string.ascii_lowercase
            else:
                result += char
                continue

            shifted_index = alphabet.index(char) - candidate_shift
            if shifted_index < 0:
                shifted_index += len_alphabet
            result += alphabet[shifted_index]

        yield candidate_shift, result


if __name__ == '__main__':
    # 暗号化させたいテキスト
    message = 'fuck you'

    # 暗号化
    encrypted_code = caesar_cipher_2(message, 3)
    print(encrypted_code)

    # 解読
    for shift_index, deciphered_text in caesar_cipher_hacking(encrypted_code):
        print(f'{shift_index:02} : {deciphered_text}')
