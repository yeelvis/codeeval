import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    line = test.split()
    index = int(line[len(line) - 1])
    alphabet = line[:len(line) - 1]     # take out last integer
    if index > len(line) - 1:           # check for if index is greater than available alphabet
        continue

    print alphabet[-1 * index]

test_cases.close()