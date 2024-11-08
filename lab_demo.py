import spellcheck

def reverse(s: str) -> str:
    result = ""
    i = 0
    while i < len(s):
        result = s[i] + result
        i += 1
    return result

def check_reversed(s: str) -> bool:
    if spellcheck.valid_word(reverse(s), "english3.txt"):
        return True
    else:
        return False
