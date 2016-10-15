from itertools import repeat, count, islice
from collections import Counter
from functools import reduce
from math import sqrt, factorial
import time

#@profile
def factors(n):
	step = 2 if n%2 else 1
	return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

#@profile
def combinations(subset):
	uniques = set(subset)
	if len(uniques) is 1 or are_divisors(uniques):
		return yeah_science(len(subset))
	else:
		count = 0
		index = 1
		for a in subset:
			for b in subset[index:]:
				if not a%b:
					count += 1
			index += 1
		return count

def are_divisors(nums):
	nums = [n for n in nums]
	nums = nums[::-1]
	index = 1
	for a in nums:
		for b in nums[index:]:
			if a%b:
				return False
		index += 1
	return True

#science, bitch!
def yeah_science(v):
	return factorial(v) // (factorial(3) * factorial(v-3))

#@profile
def answer(numbers):
	triples = 0
	counts = Counter(numbers)
	numbers = numbers[::-1]

	# if we have only one unique number
	# or if all numbers are actual divisors already
	# then add their counts and use the formula
	if len(counts) is 1 or are_divisors(counts):
		v = sum(counts.values())
		return yeah_science(v)

	for n in numbers:
		print(n)
		all_factors = factors(n)
		subset = [a for a in all_factors for _ in range(counts[a])]
		subset = sorted(subset, reverse = True)
		subset.pop(0)
		triples += combinations(subset)

		counts[n] -= 1
		if counts[n] is 0:
			del counts[n]
			if are_divisors(counts):
				v = sum(counts.values())
				return triples + yeah_science(v)

	return triples

#num_list = list(range(1,9999))
num_list = []
for _ in range(1000):
	num_list.append(1)
num_list.append(3)
#num_list.append(7)
#num_list = [1,2,3,4,5,6]

start = time.time()
print(answer(num_list))
end = time.time()
print((end - start))


# 12 6 3
# 12 6 2
# 12 6 1
# 12 4 2
# 12 4 1
# 12 3 1
# 12 2 1
# 6  3 1
# 6  2 1
# 4  2 1