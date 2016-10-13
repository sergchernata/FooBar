from itertools import combinations
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

# fastest
#@profile
def answer(l):
	triples = 0
	l.reverse()
	index = 0

	for num in l:
		all_factors = factors(num)
		subset = l[index:]
		subset = [x for x in subset if x in all_factors]
		
		if len(subset) > 1:
			subset.pop(0)
			combo = combinations(subset, 2)
			triples += sum(1 for d in combo if d[0]%d[1] is 0)
		
		index += 1

	return triples

num_list = list(range(1,9999))
#num_list = [1,2,3,4,5,6,12]

start = time.time()
print(answer(num_list))
end = time.time()
print((end - start))