def answer(l):
    triples = 0
    nums = list(set(l))

    if len(nums) == 1:
        return 1
    else:
        nums.reverse()
        for x in nums:
            high = x / 2
            even = x % 2 == 0

            if even:
                triples += 1

    return triples

print(answer([1, 2, 3, 4, 5, 6]))