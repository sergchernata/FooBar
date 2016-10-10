def answer(M, F):
    cycles = 0
    m = f = 1
    m_goal = int(M)
    f_goal = int(F)
    condition = m == m_goal and f == f_goal

    while not condition:

        cycles += 1

    return str(cycles) if condition else 'impossible'