def answer(total_lambs):
    stingy = []
    generous = []
    max = int(total_lambs / 2)
    x = 1

    while x < max:
        rule_1 = x == 1 and 1 not in stingy
        rule_2 = len(stingy) < 1 or stingy[-1] * 2 >= x
        rule_3 = len(stingy) < 2 or len(stingy) >= 2 and x >= stingy[-1] + stingy[-2]

        if rule_1 or rule_2 and rule_3:
            stingy.append(x)
        else:
            x += 1

        print(stingy)
        print('x: ',x,' 1: ',rule_1,' 2: ',rule_2,' 3: ',rule_3,)

    #print(generous)
    print(len(stingy) - len(generous))

answer(10)