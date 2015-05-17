for i in range(1,13):
    row = []
    for j in range(1,13):
        if j == 1:
            row.append(str(i * j))
        else:
            row.append("{:>4}".format(str(i * j)))

    print ''.join(row)
