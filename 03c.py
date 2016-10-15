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
	index = 1
	for a in subset:
		for b in subset[index:]:
			if not a%b:
				yield 1
		index += 1

#@profile
def answer(numbers):
	triples = 0
	counts = Counter(numbers)
	numbers = numbers[::-1]

	if len(counts) is 1:
		for c in counts:
			v = counts[c]
			return factorial(v) // (factorial(3) * factorial(v-3))

	for n in numbers:
		all_factors = factors(n)
		subset = [a for a in all_factors for _ in range(counts[a])]
		subset = sorted(subset, reverse = True)
		subset.pop(0)
		triples += sum(combinations(subset))
		counts[n] -= 1

	return triples

num_list = list(range(1,9999))
# num_list = []
# for _ in range(3):
# 	num_list.append(1)
# num_list.append(3)
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