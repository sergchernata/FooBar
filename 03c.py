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
	subset.pop(0)
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
		all_factors = factors(n)
		subset = [a for a in all_factors for _ in range(counts[a])]
		subset = sorted(subset, reverse = True)

		uniques = set(subset)
		v = len(subset)
		if v > 2 and (len(uniques) is 1 or are_divisors(uniques)):
			triples += yeah_science(v)
			numbers = [item for item in numbers if item != n]
			counts[n] = 0

		else:
			triples += combinations(subset)
			counts[n] -= 1

		if counts[n] is 0:
			del counts[n]
			v = sum(counts.values())
			if v > 2 and are_divisors(counts):
				return triples + yeah_science(v)

	return triples

#num_list = list(range(1,9999))
# num_list = []
# for _ in range(1000):
# 	num_list.append(1)
# num_list.append(3)
# num_list.append(7)
#num_list = [1,1,1,1,1,1,1,3,3,7,7]

print(answer([1,1,1]) is 1)
print(answer([1,2,3,4,5,6]) is 3)
print(answer([1,2,3,4,5,6,6]) is 8)
print(answer([1,2,3,4,5,6,12]) is 10)

# testing the math
s = answer([1,1,1,1,1,1,1,3,3,7,7])
a = answer([1,1,1,1,1,1,1,3,3])
b = answer([1,1,1,1,1,1,1,7,7])
print(s, a, b, ' - ', s is a + b)

s = answer([1,1,1,1,1,1,1,3,7])
a = answer([1,1,1,1,1,1,1,3])
b = answer([1,1,1,1,1,1,1,7])
print(s, a, b, ' - ', s is a + b)

start = time.time()
#print(answer(num_list))
end = time.time()
print((end - start))
