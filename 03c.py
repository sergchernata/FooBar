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
                high = x / 2
                subset = nums[nums.index(high):]
                while len(subset) > 1:

                print(subset)

                triples += len(divisors) - 1

    return triples

answer([1, 2, 3, 4, 5, 6, 12])