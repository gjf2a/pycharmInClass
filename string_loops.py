def print_letters_backwards(s: str):
    i = 0
    while i < len(s):
        print(f"{i} ({-i-1}): [{s[-i-1]}]")
        i += 1

def count_a(s: str) -> int:
    result = 0
    i = 0
    while i < len(s):
        if s[i] == 'a':
            result += 1
        i += 1
    return result

def word_count(s: str) -> int:
    result = 0
    i = 0
    while i < len(s):
        bc = s[i:i+2]
        if bc[0].isalpha() and (len(bc) == 1 or not bc[1].isalpha()):
            result += 1
        i += 1
    return result

def with_prefix(long_text: str, prefix: str) -> str:
    result = ""
    i = 0
    while i < len(long_text):
        if (i == 0 or long_text[i - 1] == ' ') and long_text[i:i + len(prefix)] == prefix:
            while i < len(long_text) and long_text[i].isalpha():
                result += long_text[i]
                i += 1
            result += " "
        else:
            i += 1
    return result

def count_prefix(long_text: str, prefix: str) -> int:
    result = 0
    i = 0
    while i < len(long_text):
        if (i == 0 or long_text[i - 1] == ' ') and long_text[i:i + len(prefix)] == prefix:
            result += 1
        i += 1
    return result


print(with_prefix('I have detained a devastating denomination of dollars.', 'de'))
print(count_prefix('I have detained a devastating denomination of dollars.', 'de'))


def repeat_word(word: str, num_repeats: int) -> str:
    result = ""
    i = 0
    while i < num_repeats:
        result += word
        i += 1
    return result


print(word_count("This is not an anagram. This is a second sentence."))

print(word_count("This is not a sentence"))

print(repeat_word('hi', 5))