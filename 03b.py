def answer(M, F):
    cycles = 0
    m = f = 1
    m_goal = int(M)
    f_goal = int(F)

    while m <= m_goal and f <= f_goal:
        m = f + m
        cycles += 1


    if m == m_goal and f == f_goal:
        return str(cycles)
    else:
        return 'impossible'

print(10**50)
print(answer('2','1'))