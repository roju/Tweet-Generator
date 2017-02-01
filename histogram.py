import re
import collections


def histogram(text):
    regex = re.compile('\w+')
    words = list()

    for line in text:
        words_in_line = regex.findall(line)
        for word in words_in_line:
            words.append(word)

    return collections.Counter(words)


def unique_words(histogram):
    return len(histogram)

def frequency(word, histogram):
    return histogram.get(word)


if __name__ == '__main__':
    text = open('huckfinn.txt', 'r')

    print(frequency("was", histogram(text)))
