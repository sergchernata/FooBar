# too memory intensive for el goog
def answer(x, y):
	size = x if x > y else y
	size = size*2
	grid = [[0] * size for i in range(size)]
	count = 1
	y_cursor = 0

	for x_cursor in range(size):
		while x_cursor >= 0:
			grid[y_cursor][x_cursor] = count
			x_cursor -= 1
			y_cursor += 1
			count += 1
		else:
			y_cursor = 0

	print(grid[x-1][y-1])

# algo rewrite
def answer(x,y):
	count = 1
	x_step = 2
	y_step = x

	for x in range(1,x):
		count += x_step
		x_step += 1

	for y in range(1,y):
		count += y_step
		y_step += 1

	print(count)

answer(1,1)