def answer(l):
    triples = 0
    nums = list(set(l))

    if len(nums) == 1:
        return 1
    elif len(nums) == 2:
        return 0
    else:
        nums.reverse()
        for x in nums:
            cursor = 1
            divisors = []
            if not x % 2:
                subset = [n for n in nums if x%n==0 and not x == n]

                while len(subset) > 1:
                    divisor = str(x)+','+str(subset[0])+','+str(subset[cursor])
                    divides = subset[0] % subset[cursor] == 0
                    if divides and divisor not in divisors:
                        divisors.append(divisor)

                    if cursor < len(subset) - 1:
                        cursor += 1
                    else:
                        cursor = 1
                        subset.pop(0)

                triples += len(divisors)
            print(divisors)
        return triples

print(answer([2, 3, 4, 5, 6, 12]))


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