class Road:
    _length = None
    _width = None

    def __init__(self, *args):
        """initialize road length and width in cm"""
        self._length = args[0]
        self._width = args[1]

    def asphalt_mass(self, *args):
        """calculate mass of asphalt for the road. args - asphalt layer thickness in cm"""
        return self._length * self._width * 1500 * args[0]/100


m11 = Road(5000, 20)
print(f'{m11.asphalt_mass(5)/1000} tons')
