
NUM_ALPHABET = {
    0: '+',
    1: '@',
    2: 'ABC',
    3: 'DEF',
    4: 'GHI',
    5: 'JKL',
    6: 'MNO',
    7: 'PQRS',
    8: 'TUV',
    9: 'WXYZ',
}


def phone_mnemonic(telephone_number: str):
    phone_number = [int(s) for s in telephone_number.replace('-', '')]

    candidate = []
    tmp = [''] * len(phone_number)

    def find_candidate_alphabet(digit: int = 0) -> None:
        if digit == len(phone_number):
            candidate.append(''.join(tmp))
        else:
            for char in NUM_ALPHABET[phone_number[digit]]:
                tmp[digit] = char
                find_candidate_alphabet(digit+1)

    find_candidate_alphabet()
    return candidate


if __name__ == '__main__':
    # 電話番号のメモニック
    n = '568-379-8466'

    for p in phone_mnemonic(n):
        if p == 'LOVEPYTHON':
            print(p)
