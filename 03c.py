from itertools import combinations
import time

def answer(l):
	triples = 0
	l.reverse()
	processed = []

	for num in l:
		subset = [n for n in l if num%n is 0]
		subset.pop(0)

		if num not in processed:
			combo = combinations(subset, 2)
			triples += sum(1 for d in combo if d[0]%d[1] is 0)
			processed.append(num)
	
	return triples

#num_list = list(range(1,9999))
num_list = [1, 2, 3, 4, 5, 6]

start = time.time()
print(answer(num_list))
end = time.time()
print((end - start))
