from itertools import combinations, repeat
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

def parse(subset, all_factors):
	result = []
	for a in all_factors:
		result += list(repeat(a, subset.count(a)))
	return result

#@profile
def answer(l):
	triples = 0
	l.reverse()
	count = Counter(l)

	for num in l:
		all_factors = factors(num)
		subset = [a for a in all_factors for _ in range(count[a])]
		subset = sorted(subset, reverse = True)
		subset.pop(0)
		combos = combinations(subset, 2)
		triples += sum(1 for d in combos if d[0]%d[1] is 0)

	return triples

num_list = list(range(1,9999))
#num_list = [1,2,3,4,5,6,6]

start = time.time()
print(answer(num_list))
end = time.time()
print((end - start))