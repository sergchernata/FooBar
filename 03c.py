def answer(l):
    triples = 0
    nums = list(l)
    nums.reverse()
    processed = []

    for x in nums:
        cursor = 1
        divisors = []
        subset = [n for n in nums if x%n==0]
        subset.pop(0)

        if x not in processed:
            while len(subset) > 1:
                divisor = str(subset[0])+','+str(subset[cursor])
                divides = subset[0] % subset[cursor] == 0
                if divides and divisor not in divisors:
                    divisors.append(divisor)

                if cursor < len(subset) - 1:
                    cursor += 1
                else:
                    cursor = 1
                    subset.pop(0)

            triples += len(divisors)
            processed.append(x)

    return triples

print(answer([1, 2, 3, 4, 5, 6, 12]))


# 12,6,3
# 12,6,2
# 12,6,1
# 12,4,2
# 12,4,1
# 12,3,1
# 12,2,1
# 6,3,1
# 6,2,1
# 4,2,1