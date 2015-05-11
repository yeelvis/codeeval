import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    numbers = test.split(',')
    counter = 1
    while True:
        if int(numbers[1]) * counter >= int(numbers[0]):
            print int(numbers[1]) * counter
            break
        else:
            counter += 1


test_cases.close()