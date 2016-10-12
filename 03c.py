from itertools import combinations
import time

def answer(l):
	triples = 0
	l.reverse()
	index = 0

	for num in l:
		subset = [n for n in l[index:] if num%n is 0]
		subset.pop(0)

		if num not in processed:
			combo = combinations(subset, 2)
			triples += sum(1 for d in combo if d[0]%d[1] is 0)

		index += 1

	return triples

#num_list = list(range(1,9999))
num_list = [1,2,2,2,2,2]

start = time.time()
print(answer(num_list))
end = time.time()
print((end - start))

# 2d,2c,2b
# 2d,2b,2a
# 2d,2a,1
# 2d,2b,1
# 2d,2c,1
# 2c,2b,2a
# 2c,2a,1
# 2b,2a,1