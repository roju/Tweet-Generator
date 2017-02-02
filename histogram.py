import re


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

    return histogram


def unique_words(histogram):
    return len(histogram)


def frequency(word, histogram):
    if word in histogram:
        return histogram.get(word)
    else:
        return 0


if __name__ == '__main__':
    text = open('huckfinn.txt', 'r')

    print(histogram(text))
