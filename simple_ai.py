import random
from typing import Dict, List


def main():
    filename = input("Enter base text filename: ")
    model = make_model_from(filename)
    done = False
    while not done:
        prompt = input("Enter single-word prompt ('quit' when done): ")
        if prompt == 'quit':
            done = True
        else:
            generated = generate_text_from(model, prompt)
            print(generated)

def generate_text_from(model: Dict[str,Dict[str,int]], prompt: str) -> str:
    sentence_enders = ['.', '!', '?']
    sentence = [prompt]
    while sentence[-1].strip()[-1] not in sentence_enders and len(sentence) < 25:
        key = pick_key_from(model, sentence)
        next_word = make_next_word_from(model, key)
        sentence.append(next_word)
    return ' '.join(sentence)


def make_next_word_from(model: Dict[str,Dict[str,int]], key: str) -> str:
    if key in model:
        successor_counts = 0
        for count in model[key].values():
            successor_counts += count
        target = random.randint(1, successor_counts)
        for successor, count in model[key].items():
            target -= count
            if target <= 0:
                return successor
    else:
        guess = random.choice(list(model))
        if type(guess) != str:
            guess = guess[0]
        return guess


def pick_key_from(model: Dict[str,Dict[str,int]], sentence: List[str]) -> str:
    if len(sentence) > 1 and random.random() > 0.2:
        key = (sentence[-2], sentence[-1])
        if key not in model:
            key = sentence[-1]
    else:
        key = sentence[-1]
    return key


def make_model_from(filename: str) -> Dict[str,Dict[str,int]]:
    with open(filename, 'r', encoding='utf8') as f:
        model = {}
        whole_file_str = f.read()
        words = whole_file_str.split()
        for i in range(len(words) - 1):
            update_count_for(model, words[i], words[i + 1])

            if i < len(words) - 2:
                update_count_for(model, (words[i], words[i + 1]), words[i + 2])
        return model


def update_count_for(model: Dict[str,Dict[str,int]], key: str, follower: str):
    if key not in model:
        model[key] = {}
    if follower not in model[key]:
        model[key][follower] = 0
    model[key][follower] += 1


if __name__ == '__main__':
    main()