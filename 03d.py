import time

def answer(maze):
	luke = LukeMazeWalker()
	luke.parse_grid(maze)
	luke.walk()
	luke.print_grid()
	return len(luke.best_solution)

class Cell(object):
	def __init__(self, x, y, is_wall = False):
		self.came_from = False
		self.is_wall = False
		self.x = x
		self.y = y
		self.g = 0
		self.h = 0
		self.f = 0

class LukeMazeWalker():
	def __init__(self):
		self.total_path = []
		self.opened = []
		self.closed = []
		self.cells = []
		self.best_solution = []
		self.walls = []
		self.test_walls = []
		self.grid = []
		self.best_grid = []
		self.grid_original = []
		self.height = 0
		self.width = 0
		self.wall_removed = False
		self.shortcut_marker = 8

	def parse_grid(self, grid):
		self.height = len(grid[0]) - 1
		self.width = len(grid) - 1
		self.grid = [list(row) for row in grid]
		self.grid_original = [list(row) for row in grid]
		self.cells = [list(row) for row in grid]

		for x in range(self.width+1):
			for y in range(self.height+1):
				if grid[x][y] == 1:
					self.walls.append( (x,y) )
					is_wall = True
				else:
					is_wall = False
				self.cells[x][y] = Cell(x,y,is_wall)

	def walk(self):
		self.opened = []
		self.closed = []
		self.opened.append(self.cells[0][0])

		while len(self.opened):
			current = self.opened[-1]
			if current.x == self.width and current.y == self.height:
				self.reconstruct()

				if not self.wall_removed:
					self.find_shortcut()

				if len(self.best_solution) <= 0 or len(self.total_path) < len(self.best_solution):
					self.best_solution = list(self.total_path)
					self.best_grid = list(self.grid)

				if not self.wall_removed or len(self.test_walls) == 0:
					return

			self.closed.append(current)
			del self.opened[-1]
			neighbors = self.get_neighbors(current)

			if not self.wall_removed:
				self.find_walls_to_test(current)

			for n in neighbors:
				if n in self.closed:
					continue

				if n in self.opened:
					if n.g > current.g + 10:
						n.g = current.g + 10
						n.h = 10 * (abs(current.x - self.width) + abs(current.y - self.height))
						n.came_from = current
						n.f = n.h + n.g
				else:
					n.g = current.g + 10
					n.h = 10 * (abs(current.x - self.width) + abs(current.y - self.height))
					n.came_from = current
					n.f = n.h + n.g
					self.opened.append( n )

		self.evaluate_dead_end(current)

	def evaluate_dead_end(self, current):
		if self.wall_removed:
			if len(self.test_walls):
				self.test_walls.pop()

		if len(self.test_walls):
			cut_x = self.test_walls[-1][0]
			cut_y = self.test_walls[-1][1]
			self.cut_wall(cut_x,cut_y)

	def find_walls_to_test(self, current):
		if current.x+2 <= self.width and self.grid[current.x+2][current.y] == 0:
			cut_x = current.x+1
			cut_y = current.y
			if (cut_x,cut_y) not in self.closed: self.test_walls.append( (cut_x,cut_y) )

		if current.y+2 <= self.height and self.grid[current.x][current.y+2] == 0:
			cut_x = current.x
			cut_y = current.y+1
			if (cut_x,cut_y) not in self.closed: self.test_walls.append( (cut_x,cut_y) )

		if current.x-2 >= 0 and self.grid[current.x-2][current.y] == 0:
			cut_x = current.x-1
			cut_y = current.y
			if (cut_x,cut_y) not in self.closed: self.test_walls.append( (cut_x,cut_y) )

		if current.y-2 >= 0 and self.grid[current.x][current.y-2] == 0:
			cut_x = current.x
			cut_y = current.y-1
			if (cut_x,cut_y) not in self.closed: self.test_walls.append( (cut_x,cut_y) )

	def cut_wall(self,x,y):
		self.grid = [list(row) for row in self.grid_original]
		self.grid[x][y] = self.shortcut_marker

		if (x, y) in self.walls:
			self.walls.remove( (x, y) )
		self.wall_removed = True
		self.walk()

	def get_neighbors(self, current):
		neighbors = []
		x = current.x
		y = current.y

		if y < self.height and (x, y+1) not in self.walls:
			neighbors.append( self.cells[x][y+1] )
		if y > 0 and (x, y-1) not in self.walls:
			neighbors.append( self.cells[x][y-1] )
		if x < self.width and (x+1, y) not in self.walls:
			neighbors.append( self.cells[x+1][y] )
		if x > 0 and (x-1, y) not in self.walls:
			neighbors.append( self.cells[x-1][y] )

		return reversed(neighbors)

	def print_grid(self):
		for x in self.best_grid:
			print(x)

		# for y in self.cells:
		# 	print(y)

	def reconstruct(self):
		self.total_path = []
		cell = self.cells[self.width][self.height]
		self.total_path = [(cell.x, cell.y)]
		while not (cell.came_from.x == 0 and cell.came_from.y == 0):
			cell = cell.came_from
			self.total_path.append((cell.x, cell.y))

		self.total_path.append((0,0))

	def find_shortcut(self):
		jump = 0
		start = 0
		end = 0
		backwards = False

		for a in self.total_path:
			for b in self.total_path:
				if self.grid[a[0]][a[1]] == 0 and self.grid[b[0]][b[1]] == 0:
					x_wall_down = a[0]+2 == b[0] and a[1] == b[1] and self.grid[a[0]+1][a[1]] == 1
					y_wall_right = a[0] == b[0] and a[1]+2 == b[1] and self.grid[a[0]][a[1]+1] == 1
					x_wall_up = a[0]-2 == b[0] and a[1] == b[1] and self.grid[a[0]-1][a[1]] == 1
					y_wall_left = a[0] == b[0] and a[1]-2 == b[1] and self.grid[a[0]][a[1]-1] == 1

					if x_wall_down or y_wall_right or x_wall_up or y_wall_left:
						index_a = self.total_path.index(a)
						index_b = self.total_path.index(b)
						dist = abs(index_a - index_b)
						if dist > jump:
							jump = dist
							start = index_a
							end = index_b

							if x_wall_down:
								shortcut = (a[0]+1, a[1])
							elif y_wall_right:
								shortcut = (a[0], a[1]+1)
							elif x_wall_up:
								backwards = True
								shortcut = (a[0]-1, a[1])
							elif y_wall_left:
								backwards = True
								shortcut = (a[0], a[1]-1)

		if jump:
			self.grid[shortcut[0]][shortcut[1]] = self.shortcut_marker
			self.best_grid = [list(row) for row in self.grid]
			if backwards:
				del self.total_path[start+1:end]
			else:
				del self.total_path[end+1:start]
			self.total_path.append(shortcut)

		self.total_path.sort()

# solves to 7
test1 = [
[0,1,1,1],
[0,0,0,1],
[1,1,0,0],
[1,1,1,0]]

# solves to 11
test2 = [
[0,0,0,0,0,0],
[1,1,1,1,1,0],
[0,0,0,0,0,0],
[0,1,1,1,1,1],
[0,1,1,1,1,1],
[0,0,0,0,0,0]]

# just visualizing the biggest one possible
test3 = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0],
[1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,0],
[1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,1,1,1,1,1],
[1,1,0,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0],
[1,1,0,1,1,0,0,0,0,1,1,1,1,1,0,1,1,1,1,1],
[0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
[0,1,1,1,1,1,1,1,1,0,1,0,1,1,1,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
[1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1],
[1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1],
[1,1,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],
[0,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1],
[1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

test4 = [
[0,0,0,0,0,0],
[0,1,1,1,1,0],
[0,0,0,1,1,0],
[1,1,0,1,1,0],
[0,0,0,1,1,0],
[1,1,1,1,1,1],
[0,0,0,0,0,0]]

# dead end with multiple possible pathways
# conditional wall breaking
test5 = [
[0,0,0,0,0,1],
[1,1,0,1,1,1],
[0,1,0,1,0,1],
[1,1,0,1,1,1],
[0,0,0,0,1,0],
[0,0,0,0,1,0]]

# narrow maze
# solves to 7
test6 = [
[0,0],
[1,1],
[0,0],
[1,0],
[0,0],
[1,0]]

# solves to 13
test7 = [
[0,0,0,0,0,0],
[1,1,1,1,1,1],
[1,1,0,1,1,1],
[0,0,0,0,1,0],
[0,0,1,1,1,0],
[1,0,0,0,0,0]]

# make sure we can find shortcuts
# from the right, not just left
test8 = [
[0,0,0,0,0,0],
[1,1,1,1,1,1],
[1,1,1,1,1,0],
[0,0,0,0,0,0],
[0,0,1,1,1,1],
[1,0,0,0,0,0]]

# long maze
# solves to 23
test9 = [
[0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0],
[1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0,0,0,1,0]]

start = time.time()
print('test 1: ',answer(test1)==7)
print('test 2: ',answer(test2)==11)
print('test 4: ',answer(test4)==12)
print('test 5: ',answer(test5)==11)
print('test 6: ',answer(test6)==7)
print('test 7: ',answer(test7)==13)
print('test 8: ',answer(test8)==19)
print('test 9: ',answer(test9)==23)
end = time.time()
print(end - start)

#print(answer(test5))