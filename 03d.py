def answer(maze):
	steps = 1
	x = y = 0
	w = h = len(maze) - 1
	maze[y][x] = 8

	while not x == y == w:
		if x < w and not maze[y][x+1] == 1:#right
			#print('right')
			x += 1
		elif y < h and not maze[y+1][x] == 1:#down
			#print('down')
			y += 1
		elif x > 0 and not maze[y][x-1] == 1:#left
			#print('left')
			x -= 1
		elif y > 0 and not maze[y-1][x] == 1:#up
			#print('up')
			y -= 1
		else:
			break

		maze[y][x] = 8
		steps += 1

	for line in maze: print(line)

	return steps

test1 = [
[0, 0, 0, 0],
[1, 1, 1, 0],
[1, 1, 1, 0],
[1, 1, 1, 0]]

test2 = [
[0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0]]

print('steps: ', answer(test1))