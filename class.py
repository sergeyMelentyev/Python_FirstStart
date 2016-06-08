import shelve

class Person:
    def __init__(self, name, job=None, pay=0):                          # object constructor
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRise(self, percent):
        self.pay *= (1.0 + percent)

class Manager(Person):
	def __init__(self, name, pay):										# customizing constructor
		Person.__init__(self, name, 'Manager', pay)
	
	def giveRise(self, percent, bonus=.10):								# customizing behavior
		Person.giveRise(self, percent + bonus)

class Department:
	def __init__(self, *args):
		self.members = list(args)

	def addMember(self, person):
		self.members.append(person)

	def giveRise(self, percent):
		for person in self.members:
			person.giveRise(percent)
	def showAll(self):
		for person in self.members:
			print(person)

sergey = Person('Sergey Melentyev', 'Engineer', 100000)
sergey.giveRise(.10)

olga = Manager('Olga Melentyeva', 'Manager', 100000)
olga.giveRise(.10)

devDep = Department(sergey)
devDep.addMember(olga)
devDep.giveRise(.10)
devDep.showAll()

db = shelve.open('persondb')											# save obj to database
for obj in (sergey, olga):
	db[obj.name] = obj
db.close()

db = shelve.open('persondb')											# update one obj in database
print('Objects from database', list(db.keys()))
olga = db['olga']
olga.giveRise(.10)
db['olga'] = olga
db.close

db = shelve.open('persondb')
print('Objects from database', list(db.keys()))
db.close
