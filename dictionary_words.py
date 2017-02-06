import random


def random_sentence(dictionary_words, sentence_length):
    dictionary_length = len(dictionary_words)
    random_string = ""

    for i in range(0, sentence_length):
        word_index = random.randint(0, dictionary_length)
        random_string += dictionary_words[word_index] + " "

    return random_string


if __name__ == '__main__':
    print("How many words?")
    sentence_length = int(raw_input())

    with open('/usr/share/dict/words') as f:
        dictionary_words = f.readlines()
        dictionary_words = [x.strip() for x in dictionary_words]

    print(random_sentence(dictionary_words, sentence_length))
