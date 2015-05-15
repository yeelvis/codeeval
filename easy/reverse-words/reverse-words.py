import sys

test_cases = open(sys.argv[1], 'r')


for test in test_cases:
    reverse_str = ''
    words = test.split()
    for i in range(len(words) - 1, -1, -1):
        reverse_str += words[i]
        if i != 0:
            reverse_str += ' '

    if reverse_str != '':
        print reverse_str