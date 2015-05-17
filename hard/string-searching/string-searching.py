import sys


def is_sub_string(search_string, pattern):
    pattern = pattern.replace("\*", "#")  # change to one character.  For distinction between wildcard

    # change to corresponding character when looking for *.  Will work if the pattern is wild card as well
    search_string = search_string.replace("*", "#")
    for p in pattern.split('*'):
        index = search_string.find(p)
        if index < 0:
            return False

        search_string = search_string[index + len(p):]

    return True


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if not test.strip():
        continue

    params = test.strip().split(',')

    print ("true" if is_sub_string(params[0], params[1]) else "false")

test_cases.close()