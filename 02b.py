def answer(total_lambs):
    stingy = []
    generous = []
    max = int(total_lambs / 2)
    last = 1

    x = 1
    while x < max:
        rule_1 = x == 1 and 1 not in stingy
        rule_2 = len(stingy) < 1 or stingy[-1] * 2 >= x
        rule_3 = len(stingy) < 2 or len(stingy) >= 2 and x >= stingy[-1] + stingy[-2]

        if rule_1 or rule_2 and rule_3:
            stingy.append(x)
        else:
            x += 1

    x = 1
    while x < max:
        rule_1 = x == 1 and 1 not in generous
        rule_2 = len(generous) < 1 or generous[-1] * 2 >= x
        rule_3 = len(generous) < 2 or len(generous) >= 2 and x >= generous[-1] + generous[-2]

        if rule_1 or rule_2 and rule_3:
            if len(generous) == 0 or x == max - 1:
                generous.append(x)
            last = x
        else:
            if last not in generous:
                generous.append(last)

        x += 1

    print(len(stingy) - len(generous))

answer(143)