class Worker:
    name = None
    surname = None
    position = None
    _income = {'wage': None, 'bonus': None}

    def __init__(self, *args):
        self.name = args[0]
        self.surname = args[1]
        self.position = args[2]
        self._income.update(args[3])


class Position(Worker):
    def get_full_name(self):
        return ' '.join([self.name, self.surname])

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


staff1 = Position('Ivan', 'Ivanov', 'engineer', {'wage': 0.5, 'bonus': 0.5})
print(f'Staff name: {staff1.name}')
print(f'Staff surname: {staff1.surname}')
print(f'Staff position: {staff1.position}')
print(f'Staff full name: {staff1.get_full_name()}')
print(f'Staff income: {staff1.get_total_income()}\n')
print(f'Staff protected income: {staff1._income}')
