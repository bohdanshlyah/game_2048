import random


class Game():
	def __init__(self):
		self.table = [0, 0, 0, 0,
					0, 0, 0, 0,
					0, 0, 0, 0,
					0, 0, 0, 0]
		self._rand_new_cells()


	def sum_digits(self, indexes):
		for i in range(4):
			if self.table[indexes[i]] != 0:
				j = i
				counter = 0
				while j > 0:
					if self.table[indexes[j]] >= self.table[indexes[j-1]]:
						if self.table[indexes[j-1]] == 0:
							value = str(self.table[indexes[j]])
							self.table[indexes[j-1]] = int(value)
							self.table[indexes[j]] = 0
						elif self.table[indexes[j]] == self.table[indexes[j-1]]:
							value1 = str(self.table[indexes[j]])
							value2 = str( self.table[indexes[j-1]])
							self.table[indexes[j-1]] = int(value1) + int(value2)
							self.table[indexes[j]] = 0
							j -= 1
						else:
							j -= 1
					else:
						j -= 1
					counter += 1
					if counter >= 10:
						break



	def move_left(self):
		self.sum_digits([0,1,2,3])
		self.sum_digits([4,5,6,7])
		self.sum_digits([8,9,10,11])
		self.sum_digits([12,13,14,15])

		self._rand_new_cells()
		self.print_common()
		print("Move left!")

	def move_right(self):
		self.sum_digits([3,2,1,0])
		self.sum_digits([7,6,5,4])
		self.sum_digits([11,10,9,8])
		self.sum_digits([15,14,13,12])

		self._rand_new_cells()
		self.print_common()
		print("Move right!")

	def move_up(self):
		self.sum_digits([0,4,8,12])
		self.sum_digits([1,5,9,13])
		self.sum_digits([2,6,10,14])
		self.sum_digits([3,7,11,15])

		self._rand_new_cells()
		self.print_common()
		print("Move up!")

	def move_down(self):
		self.sum_digits([12,8,4,0])
		self.sum_digits([13,9,5,1])
		self.sum_digits([14,10,6,2])
		self.sum_digits([15,11,7,3])

		self._rand_new_cells()
		self.print_common()
		print("Move down!")

	def print_common(self):
		column = 0
		raw = ""
		for i in self.table:
			blanks = " " * (4-len(str(i)))
			if column != 3:
				raw += blanks + str(i) + " "
				column += 1
			else:
				raw += blanks + str(i) + "\n"
				print(raw)
				raw = ""
				column = 0

	def _rand_new_cells(self):
		counter = 0
		while True:
			if 0 in self.table:
				if counter != 2:
					index = random.randint(0, len(self.table)-1)
					value = random.randint(2, 4)
					if value != 3:
						if self.table[index] == 0:
							self.table[index] = value
							counter += 1
				else: 
					break
			else:
				break


def run_game(new_game):
	while True:
		if new_game:
			table = Game()
			table.print_common()
			new_game = False
		else:
			key = input()
			if key == "a":
				table.move_left()
			elif key == "d":
				table.move_right()
			elif key == "w":
				table.move_up()
			elif key == "s":
				table.move_down()




if __name__=="__main__":
	new_game = True
	run_game(new_game)