from operator import xor
import itertools as IT
import functools

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
    chksm = 0
    end = start + length * (length - 1)
    line = prev_line = length

    while start <= end:
        if line == 0:
            start += length - prev_line
            chksm ^= start
            line = prev_line = prev_line - 1
        else:
            chksm ^= start

        start += 1
        line -= 1

    return chksm

# let's get weird with it
def answer(start, length):
    c = IT.count(0)
    s = start
    l = length
    nums = [list(range(s+l*n, s+l*n+l-next(c))) for n in range(l)]
    nums = [item for sublist in nums for item in sublist]
    return functools.reduce(xor, nums)

print(answer(17,4))
