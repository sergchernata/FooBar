from itertools import repeat, count, islice
from collections import Counter
from functools import reduce
from math import sqrt
import time

# sexy but slow as fuck
def answer(l):
	l.reverse()
	combo = combinations(l, 3)
	return sum(1 for d in combo if d[0]%d[1] is 0 and d[1]%d[2] is 0)

#@profile
def factors(n):
	step = 2 if n%2 else 1
	return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

#@profile
def combinations(subset):
	for a in subset:
		subset.pop(0)
		for b in subset:
			if not a%b: yield 1

#@profile
def is_prime(n):
	if n < 2: return False
	for number in islice(count(2), int(sqrt(n)-1)):
		if not n%number:
			return False
	return True

#@profile
def answer(numbers):
	triples = 0
	counts = Counter(numbers)
	numbers = [n for n in numbers if not (counts[n] is 1 and is_prime(n))]
	numbers = numbers[::-1]

	for n in numbers:
		all_factors = factors(n)
		subset = [a for a in all_factors for _ in range(counts[a])]
		subset = sorted(subset, reverse = True)
		subset.pop(0)
		triples += sum(combinations(subset))

	return triples

num_list = list(range(1,9999))
#num_list = [1,2,3,4,5,6,6]

start = time.time()
print(answer(num_list))
end = time.time()
print((end - start))