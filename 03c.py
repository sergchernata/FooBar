from itertools import combinations
import time

# sexy but basically slow as fuck
def answer(l):
	triples = 0
	l.reverse()

	combo = combinations(l, 3)
	triples += sum(1 for d in combo if d[0]%d[1] is 0 and d[1]%d[2] is 0)

	return triples

# fastest
def answer(l):
	triples = 0
	l.reverse()
	index = 0

	for num in l:
		subset = [n for n in l[index:] if num%n is 0]
		subset.pop(0)

		if len(subset) > 1:
			combo = combinations(subset, 2)
			triples += sum(1 for d in combo if d[0]%d[1] is 0)
			index += 1

	return triples

#num_list = list(range(1,9999))
num_list = [1,2,3,4,5,6,6]

start = time.time()
print(answer(num_list))
end = time.time()
print((end - start))