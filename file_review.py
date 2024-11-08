def read_from_file(filename: str):
    with open(filename) as file_input:
        for line in file_input:
            print(line.rstrip())

def line_counter(filename: str) -> int:
    num_lines = 0
    with open(filename) as file_input:
        for line in file_input:
            num_lines += 1
    return num_lines

def word_counter(filename: str) -> int:
    num_words = 0
    with open(filename) as file_input:
        for line in file_input:
            words = line.split()
            num_words += len(words)
    return num_words

def copy_file(input_filename: str, output_filename: str):
    with open(input_filename) as file_input:
        with open(output_filename, 'w') as file_output:
            for line in file_input:
                file_output.write(line)

def text_to_file(output_filename: str):
    with open(output_filename, 'w') as file_output:
        done = False
        while not done:
            line = input("> ")
            if len(line) == 0:
                done = True
            else:
                file_output.write(f"{line}\n")
