def answer(l):
    triples = 0
    nums = list(set(l))

    if len(nums) == 1:
        return 1
    else:
        nums.reverse()
        for x in nums:
            divisors = []

            if not x % 2:
                divisors.append(x // 2)
                if divisors[-1] in nums:
                    subset = nums[nums.index(divisors[-1]):]
                    while len(subset) > 0:
                        if x % subset[0] == 0 and subset[0] not in divisors:
                            divisors.append(subset[0])
                        subset.pop(0)

                    triples += len(divisors) - 1

    return triples

answer([1, 2, 3, 4, 5, 6])