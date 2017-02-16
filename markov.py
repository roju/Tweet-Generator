import sys
import random

class Dictogram(dict):

    def __init__(self, iterable=None):
        super(Dictogram, self).__init__()
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.tokens += 1
            if item in self:
                self[item] += 1
            else:
                self[item] = 1
                self.types += 1
        pass

    def count(self, item):
        return self.get(item, 0)
        pass

    def return_random_word(self):
        # Another way:  Should test: random.choice(histogram.keys())
        random_key = random.sample(self, 1)
        return random_key[0]


    def random_word_weighted(self):
        words_in_original_text = sum(self.values())
        index = random.randint(1, words_in_original_text)
        count = 0

        for key in self:
            count += self[key]
            if count >= index:
                return key


def markov_model(data):
    markov_model = {}

    for i in range(0, len(data)-1):
        if data[i] in markov_model:
            # We have to just append to the existing histogram
            markov_model[data[i]].update([data[i+1]])
        else:
            markov_model[data[i]] = Dictogram([data[i+1]])
    return markov_model


if __name__ == '__main__':
    d = Dictogram(sys.argv[1:])
    print(d)
