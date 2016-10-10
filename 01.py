def answer(x, y):
	if len(x) > len(y):
		diff = list(set(x) - set(y))
	else:
		diff = list(set(y) - set(x))
	return diff[0]

print(answer(x,y))