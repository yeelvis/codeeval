import sys


def remove_char(sentence, elements):
    tmp_str = sentence
    for character in elements:
        tmp_str = tmp_str.replace(character, "")
        tmp_str = tmp_str.replace(character.upper(), "")

    return tmp_str

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    params = test.split(", ")
    print remove_char(params[0], params[1])

test_cases.close()