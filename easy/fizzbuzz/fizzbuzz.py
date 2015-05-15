import sys


def runner(x,y, count):
    str_builder = []
    for i in range(1, count + 1):
        if i % x == 0 and i % y == 0:
            str_builder.append("FB")
        elif i % x == 0:
            str_builder.append("F")
        elif i % y == 0:
            str_builder.append("B")
        else:
            str_builder.append(str(i))

    print ' '.join(str_builder)


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    fields = test.split()
    runner(int(fields[0]),int(fields[1]),int(fields[2]))


test_cases.close()



