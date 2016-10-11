def answer(M, F):
    cycles = 0
    n = sorted([int(M),int(F)])
    m = n[1]
    f = n[0]

    while m >= 1 and f >= 1:

        if int(m % f) > 0:
            c = int(m / f)
            m -= f * c
            cycles += c

        if m > f:
            m -= f
        elif m < f:
            f -= m
        elif m == f:
            break

        cycles += 1

    return str(cycles) if m == f == 1 else 'impossible'

print(answer('3','10'))