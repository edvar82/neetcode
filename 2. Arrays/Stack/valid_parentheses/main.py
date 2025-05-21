from typing import List

def isValid(s: str) -> bool:
    back_arr = []
    pairs = {
        ')': '(',
        '}': '}',
        ']': '['
    }

    for ch in s:
        if ch not in pairs:
            back_arr.append(ch)
        elif not back_arr or back_arr[-1] != pairs[ch]:
            return False
        else:
            back_arr.pop()

    return len(back_arr) == 0

s = "([])"

isValid(s)