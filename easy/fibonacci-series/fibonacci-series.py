import sys


def fib_series(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1

    last_digit = 1
    second_last_digit = 0
    current = 0
    for i in range(2, index + 1):
        current = last_digit + second_last_digit
        second_last_digit = last_digit
        last_digit = current

    return current


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print fib_series(int(test))

test_cases.close()