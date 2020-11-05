class Car:
    speed = None
    color = None
    name = None
    is_police = False

    def go(self):
        if self.speed is None:
            self.speed = 40
        return print(f'The car {self.name} drove.')

    def stop(self):
        self.speed = 0
        return print(f'The car {self.name} stopped.')

    def turn(self, direction):
        return print(f'The car {self.name} turned to the {direction}')

    def show_speed(self):
        return print(f'Current speed is {self.speed}')


class TownCar(Car):
    def __init__(self):
        self.is_police = False
        self.name = 'Town car'

    def show_speed(self):
        if self.speed > 60:
            print(f'Current speed({self.speed}) is more than speed limit.')
        else:
            print(f'Current speed is {self.speed}')


class SportCar(Car):
    def __init__(self):
        self.is_police = False
        self.color = 'Red'
        self.name = 'Viper'
    speed = 90


class WorkCar(Car):
    def __init__(self):
        self.is_police = False
        self.name = 'Track'

    def show_speed(self):
        if self.speed > 40:
            print(f'Current speed({self.speed}) is more than speed limit.')
        else:
            print(f'Current speed is {self.speed}')


class PoliceCar(Car):
    def __init__(self):
        self.name = 'Police'
        self.is_police = True
        self.color = 'Blue'


print('Police')
police = PoliceCar()
print(f'This car is police - {police.is_police}')
police.speed = 90
police.show_speed()
police.turn('left')

print('\nTrack')
track = WorkCar()
print(f'This car is police - {track.is_police}')
track.go()
track.show_speed()
track.speed = 60
track.show_speed()
track.stop()
track.show_speed()

print('\nMy car')
my_car = TownCar()
my_car.color = 'black'
my_car.go()
my_car.turn('right')
my_car.show_speed()
my_car.speed = 70
my_car.show_speed()
