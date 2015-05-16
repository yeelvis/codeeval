import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    sum = 0
    for digit in test.strip():
        sum += int(digit)
    print sum


test_cases.close()