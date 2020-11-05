class Stationery:
    title = None

    @staticmethod
    def draw(self):
        return print('Start drawing.')


class Pen(Stationery):
    def __init__(self):
        self.title = 'Pen'

    def draw(self):
        return print(f'Start drawing by {self.title}. It will be difficult to erase.')
    pass


class Pencil(Stationery):
    def __init__(self):
        self.title = 'Pencil'

    def draw(self):
        return print(f'Start drawing by {self.title}.')
    pass


class Handle(Stationery):
    def __init__(self):
        self.title = 'Handle'

    def draw(self):
        return print(f'Start drawing by {self.title}. Are you sure?')
    pass


take_pen = Pen()
take_pen.draw()
print('\n')
take_pencil = Pencil()
take_pencil.draw()
print('\n')
take_handle = Handle()
take_handle.draw()
