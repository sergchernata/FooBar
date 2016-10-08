def answer(total_lambs):
    stingy = [1,1,2,3]
    generous = [1,2,4]

    i = 4
    while i < total_lambs:
        new = stingy[-1] + stingy[-2]

        if sum(stingy) + new > total_lambs:
            break

        stingy.append(new)
        i = new

    i = 5
    while i < total_lambs:
        new = generous[-1] * 2

        if sum(generous) + new > total_lambs:
            break

        generous.append(new)
        i = new

    return len(stingy) - len(generous)

print(answer(1000000))