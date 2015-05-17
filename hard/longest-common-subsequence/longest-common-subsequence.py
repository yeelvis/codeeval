import sys


def find_lcs(str1, str2):
    length_matrix = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]
    for i, x in enumerate(str1):
        for j, y in enumerate(str2):
            if x == y:
                length_matrix[i+1][j+1] = length_matrix[i][j] + 1
            else:
                length_matrix[i+1][j+1] = max(length_matrix[i][j+1], length_matrix[i+1][j])

    lcs = ""

    x = len(str1)
    y = len(str2)

    while x != 0 and y != 0:
        if length_matrix[x][y] == length_matrix[x-1][y]:
            x -= 1
        elif length_matrix[x][y] == length_matrix[x][y-1]:
            y -= 1
        else:
            lcs = str2[y-1] + lcs
            x -= 1
            y -= 1

    return lcs

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if not test.strip():
        continue

    if ";" not in test:
        continue

    params = test.split(';')
    if not params[0] or not params[1]:
        continue

    print find_lcs(params[0], params[1])

test_cases.close()