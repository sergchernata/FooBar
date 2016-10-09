# two loops
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

# one loop
def answer(start, length):
    chksm = skip = None
    end = start + length * (length - 1) + 1
    line = prev_line = length

    for x in range(start,end):
        if line == 0:
            if skip == None: skip = length - prev_line

            if skip <= 0:
                chksm ^= x
                line = prev_line = prev_line - 1
                skip = None
                line -= 1
            else:
                skip -= 1
        else:
            chksm = chksm^x if chksm != None else x
            line -= 1

    return chksm

print(answer(17,4))
