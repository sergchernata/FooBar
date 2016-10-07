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

answer(5,10)