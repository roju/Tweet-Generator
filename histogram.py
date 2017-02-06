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
    return histogram.get(word, 0)


def print_sorted_histogram(histogram):
    for w in sorted(histogram, key=histogram.get, reverse=True):
        print(w, histogram[w])


if __name__ == '__main__':
    text = open('huckfinn.txt', 'r')

    print_sorted_histogram(histogram(text))
