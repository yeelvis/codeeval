import sys


def check_largest(current, contender):
    if current >= contender:
        return current
    else:
        return contender


def find_largest_sum(sequences):
    current_largest = int(sequences[0])
    pt = 0
    for i in sequences:
        tmp_sum = int(i)
        current_largest = check_largest(current_largest, tmp_sum)
        pt += 1
        if pt == len(sequences):
            current_largest = check_largest(current_largest, tmp_sum)
        for j in range(pt, len(sequences)):
            tmp_sum += int(sequences[j])
            current_largest = check_largest(current_largest, tmp_sum)

    return current_largest


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if not test.strip():
        continue
    print find_largest_sum(test.strip().split(','))

test_cases.close()