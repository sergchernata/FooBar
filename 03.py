from operator import xor
import itertools as IT
from functools import reduce
import time
import math

# def answer(start, length):
# 	count = start
# 	checksum = -1
# 	x_axis = range(length + 1)
# 	y_axis = reversed(range(length))

# 	for y in y_axis:
# 		line = y + 1
# 		for x in x_axis:
# 			if line > 0:
# 				if checksum > -1:
# 					checksum ^= count
# 				else:
# 					checksum = start
# 				line -= 1
# 				count += 1
# 			else:
# 				count += length - x
# 				break

# 	return checksum

# two ways of doing the same thing
def f(a):
    #res = [a, 1, a+1, 0]
    #return res[a%4]
	if a%4 == 0:
		return a
	elif a%4 == 1:
		return 1
	elif a%4 == 2:
		return a+1
	else:
		return 0

# one loop
def answer(start, length):
	chksm = 0
	end = start + length * (length - 1)
	line = prev_line = length
	
	while start <= end:
		#chksm ^= reduce(lambda x, y: x^y, list(range(start,start+line)))
		#chksm ^= reduce(xor, list(range(start,start+line)))
		#for x in range(start,start+line): chksm ^= x
		chksm ^= f(start+line-1) ^ f(start-1)
		start += line + length - prev_line
		line = prev_line = prev_line - 1

	return chksm

# let's get weird with it
# def answer(start, length):
# 	c = IT.count(0)
# 	s = start
# 	l = length
# 	nums = [list(range(s+l*n, s+l*n+l-next(c))) for n in range(l)]
# 	nums = [item for sublist in nums for item in sublist]
# 	return reduce(xor, nums)

start = time.time()
print(answer(17,4))
end = time.time()
print(end - start)
