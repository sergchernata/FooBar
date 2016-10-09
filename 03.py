def answer(start, length):
    count = start
    checksum = -1
    x_axis = range(length + 1)
    y_axis = reversed(range(length))

    for y in y_axis:
        line = y + 1
        for x in x_axis:
            if line > 0:
                if checksum > -1:
                    checksum ^= count
                else:
                    checksum = start
                line -= 1
                count += 1
            else:
                count += length - x
                break

    return checksum

def answer(start, length):
    checksum = skip = -1
    end = start + 4 * (length - 1) + 1
    line = prev = length

    for x in range(start,end):

        if line == 0:
            if skip == -1: skip = length - prev

            if skip <= 0:
                checksum ^= x
                line = prev = prev - 1
                skip = -1
                line -= 1
            else:
                skip -= 1
        else:
            checksum = checksum^x if checksum != -1 else x
            line -= 1

    return checksum

print(answer(17,4))
