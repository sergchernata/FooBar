def answer(M, F):
    cycles = 0
    m = int(M)
    f = int(F)

    while (m > 1 or f > 1) and (m > 0 and f > 0):
        if m > f:
            m = m - f
        elif m == f:
            break
        else:
            f = f - m
        cycles += 1

    if m == f == 1:
        return str(cycles)
    else:
        return 'impossible'

print(answer('4','7'))