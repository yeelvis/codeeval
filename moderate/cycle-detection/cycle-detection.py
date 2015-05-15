import sys

def check_cycle(sequence, starting_point, length):
    end_point = starting_point + length
    if end_point >= len(sequence):
        return False
    else:
        for i in range(length):
            indexA = starting_point + i
            indexB = end_point + i
            if indexA >= len(sequence) or indexB >= len(sequence):
                return False
            elif sequence[indexA] != sequence[indexB]:
                return False
        return True

def cycle_detection(sequence):
    for i in range(len(sequence)):
        for j in range(1, len(sequence)):
            if check_cycle(sequence, i, j):
                return sequence[i:i + j]


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # cycle_detection()
    arr = map(int, test.split())
    print ' '.join(str(x) for x in cycle_detection(arr))
test_cases.close()


