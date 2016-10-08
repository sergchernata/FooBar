def answer(start, length):
    count = start
    checksum = -1
    x_axis = range(length)
    y_axis = reversed(range(length + 1))

    for y in y_axis:
        line = y

        for x in x_axis:
            if line > 0:
                if checksum > -1:
                    checksum ^= count
                else:
                    checksum = start
                line -= 1

            count += 1

    return checksum

print(answer(17,4))