def answer(M, F):
    cycles = 0
    m = int(M)
    f = int(F)

    while m >= 1 and f >= 1:

        if m > f and int(m % f) > 0:
            c = int(m / f)
            m -= f * c
            cycles += c
        elif m < f and int(f % m) > 0:
            c = int(f / m)
            f -= m * c
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