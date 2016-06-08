class Worker:
    def __init__(self, name, job=None, pay=0):                          # object constructor
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]                                    # ['Sergey', 'Melentyev']

    def giveRise(self, percent):
        self.pay *= (1.0 + percent)


sergey = Worker('Sergey Melentyev', 'Engineer', 100000)
sergey.giveRise(.10)
