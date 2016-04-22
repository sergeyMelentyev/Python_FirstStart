class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]                                    # ['Sergey', 'Melentyev']

    def giveRise(self, percent):
        self.pay *= (1.0 + percent)

sergey = Worker('Sergey Melentyev', 100000)
sergey.giveRise(.10)
