def find_reversed_string(smaller_string, larger_string):
    reversed_string = ""
    index = len(smaller_string)

    while(index > 0):
        index -= 1
        reversed_string += smaller_string[index]

    if reversed_string in larger_string:
        return True
    return False

if __name__ == '__main__':
    print(find_reversed_string("abc", "i am cba banana"))
