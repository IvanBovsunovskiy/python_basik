class Cell:
    cell_number = None
    string_cells = ''

    def __init__(self, num):
        try:
            if not(num is None):
                self.cell_number = num
        except TypeError:
            self.cell_number = 0

    def __add__(self, other):
        if isinstance(other, Cell):
            self.cell_number += other.cell_number
            return self
        else:
            print('You trying to get sum of cell and something else.')

    def __sub__(self, other):
        if isinstance(other, Cell):
            if self.cell_number > other.cell_number:
                self.cell_number = self.cell_number - other.cell_number
                return self
            else:
                print('Number of cells you want to subtract is more than current number of cells.')
        else:
            print('You trying to get sum of cell and something else.')

    def __mul__(self, other):
        if isinstance(other, Cell):
            self.cell_number *= other.cell_number
            return self
        else:
            print('You trying to get sum of cell and something else.')

    def __truediv__(self, other):
        if isinstance(other, Cell):
            self.cell_number = int(self.cell_number / other.cell_number)
            return self
        else:
            print('You trying to get sum of cell and something else.')

    def __eq__(self, other):
        if self.cell_number == other.cell_number:
            return True
        else:
            return False

    def make_order(self, cell_in_line):
        temp = self.cell_number
        while temp > 0:
            temp -= cell_in_line
            if temp < 0:
                self.string_cells += f'{"*" * (temp + cell_in_line)}\n'
                print(1)
            else:
                self.string_cells += f'{"*" * cell_in_line}\n'
        return self.string_cells


a = Cell(5)
b = Cell(3)
c = Cell(0)
c = a - b
print(c is a, f'c.cell_number = {c.cell_number}   a.cell_number = {a.cell_number}', sep=' --- ')

c = a + b
print(c is b, f'c.cell_number = {c.cell_number}   b.cell_number = {b.cell_number}', sep=' --- ')

c = a * b
print(c is a, f'c.cell_number = {c.cell_number}   a.cell_number = {a.cell_number}', sep=' --- ')

print('a =', a.cell_number, 'b =', b.cell_number, 'c =', c.cell_number, sep=' ')
print(c.make_order(4))

c = a / b
print(c is a, f'c.cell_number = {c.cell_number}   a.cell_number = {a.cell_number}', sep=' --- ')
