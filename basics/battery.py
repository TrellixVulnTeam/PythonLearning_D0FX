# use the instance as an attribute
class Battery():

	def __init__(self, battery_size=70):
		self.battery_size = battery_size

	def describe_battery(self):
		print('This car has a ' + str(self.battery_size) + '-kwh battery.')