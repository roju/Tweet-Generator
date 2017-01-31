import random


def rearranged_string(input_string):
    words = input_string.split()
    random.shuffle(words)
    return " ".join(words)


if __name__ == '__main__':
    input_string = raw_input()
    print(rearranged_string(input_string))
