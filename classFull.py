# PIZZA SHOP INTERFACE
class Employee:																				# declare a super class
	"""docstring for Employee"""
	def __init__(self, name, salary=0):														# custom init overloader
		self.name = name																	# class attribute
		self.salary = salary
	def giveRise(self, percent):															# class method
		self.salary = self.salary + (self.salary * percent)
	def work(self):
		print(self.name, 'does stuff')

class Chef(Employee):																		# sub class
	"""docstring for Chef"""
	def __init__(self, name):																# custom init overloader
		Employee.__init__(self, name, 50000)
	def work(self):																			# custom method overloader
		print(self.name, 'makes food')

class Server(Employee):
	"""docstring for Server"""
	def __init__(self, name):
		Employee.__init__(self, name, 40000)
	def work(self):
		print(self.name, 'interfaces with customer')

class PizzaRobot(Chef):
	"""docstring for PizzaRobot"""
	def __init__(self, name):
		Chef.__init__(self, name)
	def work(self):
		print(self.name, 'makes pizza')

# CUSTOMER INTERFACE
class Customer:																				# declare a new super class
	"""docstring for Customer"""
	def __init__(self, name):																# custom init overloader
		self.name = name
	def order(self, server):																# class method
		print(self.name, 'order from', server)
	def pay(self, server):
		print(self.name, 'pays for item to', server)

class Oven:																					# declare a new super class
	"""docstring for Oven"""
	def bake(self):																			# custom init overloader
		print('oven bakes')

class PizzaShop:
	"""docstring for PizzaShop"""
	def __init__(self):
		self.server = Server('Pat')
		self.chef = Chef('Bob')
		self.oven = Oven()
	def order(self, name):
		customer = Customer(name)
		customer.order(self.server)
		self.chef.work()
		self.oven.bake()
		customer.pay(self.server)
