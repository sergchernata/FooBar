import time

def answer(maze):
	luke = LukeMazeWalker()
	luke.parse_grid(maze)
	luke.solve()
	#luke.cut_wall()
	#luke.print_grid()

	return sum(x.count(8) for x in maze)

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
		self.opened = [Cell(0,0)]
		self.closed = []
		self.cells = []
		self.walls = []
		self.grid = []
		self.height = 0
		self.width = 0

	def parse_grid(self, grid):
		self.height = self.width = len(grid) - 1

		self.grid = grid
		self.cells = grid[:]
		for x in range(self.width+1):
			for y in range(self.height+1):
				if grid[x][y] == 1:
					self.walls.append( (x,y) )
					is_wall = True
				else:
					is_wall = False
				self.cells[x][y] = Cell(x,y,is_wall)

	def solve(self):
		while len(self.opened):
			current = self.opened[-1]
			if current.x == self.width and current.y == self.height:
				return self.reconstruct()

			self.closed.append(current)
			del self.opened[-1]
			neighbors = self.get_neighbors(current)
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

	def get_neighbors(self, current):
		neighbors = []
		x = current.x
		y = current.y

		if x < self.width and (x+1, y) not in self.walls:
			neighbors.append( self.cells[x+1][y] )
		if x > 0 and (x-1, y) not in self.walls:
			neighbors.append( self.cells[x-1][y] )
		if y < self.height and (x, y+1) not in self.walls:
			neighbors.append( self.cells[x][+1] )
		if y > 0 and (x, y-1) not in self.walls:
			neighbors.append( self.cells[x][-1] )

		return neighbors

	def print_grid(self):
		for x in self.grid:
			print(x)

		for y in self.cells:
			print(y)

	def reconstruct(self):
		cell = self.cells[self.width][self.height]
		total_path = [(self.width, self.height)]
		while not (cell.came_from.x == 0 and cell.came_from.x == 0):
			cell = cell.came_from
			total_path.append((cell.x, cell.y))

		total_path.append((0, 0))

		for x in total_path:
			print(x)




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

test3 = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

test4 = [
[0, 0, 0, 0, 0, 1],
[1, 1, 0, 0, 0, 1],
[0, 0, 0, 1, 0, 0],
[0, 1, 1, 0, 0, 1],
[0, 1, 0, 0, 1, 0],
[0, 1, 0, 0, 0, 2]]

print('steps: ', answer(test1))