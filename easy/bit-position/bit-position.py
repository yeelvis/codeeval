import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    line = test.split(',')
    binary = "{0:0b}".format(int(line[0]))
    if binary[-1 * int(line[1])] == binary[-1 * int(line[2])]:
        print "true"
    else:
        print "false"

test_cases.close()

