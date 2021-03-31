class Cat:
	__name = "Kitty”			
	def get_name(self):
		return self.__name
	def set_name(self, name):
		self.__name = name
cat = Cat()
print(cat.get_name())
cat.set_name("Misty")
print(cat.get_name())
Kitty
Misty

