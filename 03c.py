from itertools import combinations
import time

def answer(l):
	triples = 0
	nums = list(l)
	nums.reverse()
	processed = []

	for x in nums:
		subset = [n for n in nums if x%n==0]
		subset.pop(0)

		if x not in processed:
			divisors = combinations(subset, 2)
			triples += sum(1 for d in divisors if d[0]%d[1]==0)
	
	return triples

num_list = list(range(1,9999))
#num_list = [1, 2, 3, 4, 5, 6, 12]

start = time.time()
print(answer(num_list))
end = time.time()
print((end - start))
