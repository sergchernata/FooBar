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
			#processed.append(x)
			# while len(subset) > 1:
			# 	divisor = str(subset[0])+','+str(subset[cursor])
			# 	divides = subset[0] % subset[cursor] == 0
			# 	if divides and divisor not in divisors:
			# 		divisors.append(divisor)

			# 	if cursor < len(subset) - 1:
			# 		cursor += 1
			# 	else:
			# 		cursor = 1
			# 		subset.pop(0)

			# triples += len(divisors)
			# processed.append(x)
	
	return triples

num_list = list(range(1,9999))
#num_list = [1, 2, 3, 4, 5, 6, 12]
#print(num_list)
start = time.time()
print(answer(num_list))
end = time.time()
print((end - start))

# 6,6,3
# 6,6,2
# 6,6,1
# 6,3,1
# 6,2,1
# 4,2,1