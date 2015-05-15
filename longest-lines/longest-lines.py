import sys
test_cases = open(sys.argv[1], 'r')
num_of_record = int(test_cases.readline())
lines = []
for test in test_cases:
    lines.append(test.rstrip('\n'))

lines.sort(lambda x,y: cmp(len(y),len(x)))

for i in range(num_of_record):
    print lines[i]
test_cases.close()