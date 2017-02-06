import random
import re


def random_word_weighted(histogram):
    weighted_id_list = list()
    word_id = 0

    for word, frequency in histogram:
        for _ in range(0, frequency):
            weighted_id_list.append(word_id)
        word_id += 1

    random_index = random.randint(0, len(weighted_id_list))
    random_word_id = weighted_id_list[random_index]

    return histogram[random_word_id][0]


def random_word_unweighted(histogram):
    return random.choice(histogram)[0]


def histogram(text):
    regex = re.compile('\w+')
    histogram = {}

    for line in text:
        words_in_line = regex.findall(line)
        for word in words_in_line:
            if word in histogram:
                histogram[word] += 1
            else:
                histogram[word] = 1

    return histogram.items()


if __name__ == '__main__':
    text = open('huckfinn.txt', 'r')

    print(random_word_weighted(histogram(text)))
