from math import pi

class Circle():
	'''Circle class'''
	def __init__(self, radius=1):
		'''Circle initialization, default radius == 1'''
		self.radius = radius

	@property
	def radius(self):
		return self._radius

	@radius.setter
	def radius(self, value):
		if value < 0:
			raise ValueError('Radius cannot be negative')
		self._radius = value

	@property
	def diameter(self):
		return self.radius * 2

	@diameter.setter
	def diameter(self, diameter):
		self.radius = diameter / 2

	@property
	def area(self):
		return pi * self.radius ** 2

	def __str__(self):
		'''Return string representation as "Cirle(self.radius)"'''
		return(f'Circle({self.radius})')

	def __repr__(self):
		return str(self)

a = Circle(3)
print(a.diameter)
print(a.area)
# a.radius = 2
# print(a.diameter)
# print(a.area)
# a.diameter = 6
# print(a.radius)
# print(a.diameter)
# print(a.area)
