from typing import List

def count_lines(filename: str) -> int:
    lines = 0
    # similar to: file_input = open(filename)
    with open(filename, encoding='utf-8') as file_input:
        for line in file_input:
            lines += 1
    return lines

def count_suffix(filename: str, suffix: str) -> int:
    suffixes = 0
    with open(filename, encoding='utf-8') as file_input:
        for line in file_input:
            no_punctuation = line.replace('.', ' ').replace('?', ' ').replace('!', ' ')
            words = no_punctuation.split()
            for word in words:
                if word.endswith(suffix):
                    suffixes += 1
    return suffixes

def with_suffix(filename: str, suffix: str) -> List[str]:
    suffix_words = []
    with open(filename, encoding='utf-8') as file_input:
        for line in file_input:
            line = line.strip()
            if line.endswith(suffix):
                suffix_words.append(line)
    return suffix_words

def word_count(filename: str) -> int:
    words = 0
    with open(filename, "r", encoding='utf-8') as file_input:
        for line in file_input:
            line_words = line.split()
            words += len(line_words)
    return words

def input_to_file(filename: str):
    with open(filename, "w") as file_output:
        done = False
        while not done:
            line = input("Enter text ('quit' to stop): ")
            if line == 'quit':
                done = True
            else:
                file_output.write(f"{line}\n")

def show_file(filename: str):
    with open(filename) as file_input:
        for line in file_input:
            line = line.rstrip()
            print(line)


def copy_file(original_name: str, new_name: str):
    with open(original_name) as file_input:
        with open(new_name, "w") as file_output:
            for line in file_input:
                file_output.write(line)