def answer(total_lambs):
    max = int(total_lambs / 2)
    last = 1
    stingy = [1,1,2,3]
    generous = [1,2,4]

    i = 4
    while i*2 < max:
        new = stingy[-1] + stingy[-2]
        stingy.append(new)
        i = new

    i = 5
    while i*2 < max:
        new = generous[-1] * 2
        generous.append(new)
        i = new

    return len(stingy) - len(generous)

answer(10)