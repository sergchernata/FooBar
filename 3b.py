def answer(M, F):
    cycles = 0
    M = int(M)
    F = int(F)

    cycles = str(M if M < F else F)

    return str(cycles) or 'impossible'