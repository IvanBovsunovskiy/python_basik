class Textile:
    v = None
    h = None

    def __init__(self, clothes):
        self.v = clothes.get('coat', None)
        self.h = clothes.get('suit', None)

    def material_consumption(self):
        if not(self.v is None):
            return self.v / 6.5 + 0.5
        elif not(self.h is None):
            return 2 * self.h + 0.3
        else:
            return 0


coat1 = Textile({'coat': 32})
print(coat1.material_consumption())

coat2 = Textile({'overcoat': 30})
print(coat2.material_consumption())

suit1 = Textile({'suit': 2})
print(suit1.material_consumption())
