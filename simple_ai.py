import random
from typing import Dict, List, Any, Tuple


def main():
    filename = input("Enter base text filename: ")
    model = SentenceModel(filename)
    done = False
    while not done:
        prompt = input("Enter single-word prompt ('quit' when done): ")
        if prompt == 'quit':
            done = True
        else:
            generated = model.generate_text_from(prompt)
            print(generated)


class SentenceModel:
    def __init__(self, filename: str):
        with open(filename, 'r', encoding='utf8') as f:
            self.single_word = {}
            self.word_pairs = {}
            whole_file_str = f.read()
            words = whole_file_str.split()
            for i in range(len(words) - 1):
                update_count_for(self.single_word, words[i], words[i + 1])

                if i < len(words) - 2:
                    update_count_for(self.word_pairs, (words[i], words[i + 1]), words[i + 2])

    def generate_text_from(self, prompt: str) -> str:
        sentence_enders = ['.', '!', '?']
        sentence = [prompt]
        while sentence[-1].strip()[-1] not in sentence_enders and len(sentence) < 25:
            key = self.pick_key_from(sentence)
            if type(key) == str:
                next_word = self.make_next_from_single(key)
            else:
                next_word = self.make_next_from_pair(key)
            sentence.append(next_word)
        return ' '.join(sentence)

    def pick_key_from(self, sentence: List[str]) -> str:
        if len(sentence) > 1 and random.random() > 0.2:
            key = (sentence[-2], sentence[-1])
            if key not in self.word_pairs:
                key = sentence[-1]
        else:
            key = sentence[-1]
        return key

    def make_next_from_single(self, key: str) -> str:
        if key in self.single_word:
            return weighted_random_pick(self.single_word[key])
        else:
            return random.choice(list(self.single_word))

    def make_next_from_pair(self, key: Tuple[str, str]) -> str:
        if key in self.word_pairs:
            return weighted_random_pick(self.word_pairs[key])
        else:
            return self.make_next_from_single(key[0])


def weighted_random_pick(successor_counter: Dict[str, int]):
    successor_counts = 0
    for count in successor_counter.values():
        successor_counts += count
    target = random.randint(1, successor_counts)
    for successor, count in successor_counter.items():
        target -= count
        if target <= 0:
            return successor


def update_count_for(model: Dict[Any,Dict[str,int]], key: Any, follower: str):
    if key not in model:
        model[key] = {}
    if follower not in model[key]:
        model[key][follower] = 0
    model[key][follower] += 1


if __name__ == '__main__':
    main()