class SimpleClass:
	'''самый простой класс на свете'''
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def sum_num(self):
	    return self.x + self.y

s = SimpleClass(1, 3)
print(s.sum_num())
