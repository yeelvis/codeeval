import sys


def find_non_repeat(word):
    char_dict = {}
    for character in word:
        if character in char_dict:
            char_dict[character] += 1
        else:
            char_dict[character] = 1

    for character in word:
        if char_dict[character] == 1:
            return character

    return ""

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        print find_non_repeat(test.strip())
    else:
        print


test_cases.close()