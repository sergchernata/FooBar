def answer(maze):
	luke = LukeMazeWalker()
	luke.parse_grid(maze)
	luke.solve()
	print(len(luke.total_path))
	#luke.print_grid()

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
		self.opened.append(self.cells[0][0])

		while len(self.opened):
			current = self.opened[-1]
			if current.x == self.width and current.y == self.height:
				self.reconstruct()
				self.cut_wall()

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

		if y < self.width and (x, y+1) not in self.walls:
			neighbors.append( self.cells[x][y+1] )
		if y > 0 and (x, y-1) not in self.walls:
			neighbors.append( self.cells[x][y-1] )
		if x < self.height and (x+1, y) not in self.walls:
			neighbors.append( self.cells[x+1][y] )
		if x > 0 and (x-1, y) not in self.walls:
			neighbors.append( self.cells[x-1][y] )

		return neighbors

	def print_grid(self):
		for x in self.grid:
			print(x)

		for y in self.cells:
			print(y)

	def reconstruct(self):
		cell = self.cells[self.width][self.height]
		self.total_path = [(cell.x, cell.y)]
		while not (cell.came_from.x == 0 and cell.came_from.y == 0):
			cell = cell.came_from
			self.total_path.append((cell.x, cell.y))

		self.total_path.append((0,0))

	def cut_wall(self):
		jump = 0
		start = 0
		end = 0
		
		for a in self.total_path:
			for b in self.total_path:
				x_wall = a[0]+2 == b[0] and a[1] == b[1]
				y_wall = a[0] == b[0] and a[1]+2 == b[1]
				if x_wall or y_wall:
					index_a = self.total_path.index(a)
					index_b = self.total_path.index(b)
					dist = abs(index_a - index_b)
					if dist > jump:
						jump = dist
						start = index_a
						end = index_b
						shortcut = (a[0]+1, a[1]) if x_wall else (a[0], a[1]+1)

		del self.total_path[end+1:start]
		self.total_path.append(shortcut)
		self.total_path.sort()


test1 = [
[0,0,0,0],
[1,1,1,0],
[1,1,1,0],
[1,1,1,0]]

test2 = [
[0,0,0,0,0,0],
[1,1,1,1,1,0],
[0,0,0,0,0,0],
[0,1,1,1,1,1],
[0,1,1,1,1,1],
[0,0,0,0,0,0]]

test3 = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

test4 = [
[0,0,0,0,0,1],
[1,1,0,0,0,1],
[0,0,0,1,0,0],
[0,1,1,0,0,1],
[0,1,0,0,1,0],
[0,1,0,0,0,2]]

answer(test2)