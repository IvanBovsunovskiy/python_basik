class ZeroDivisionErr(ZeroDivisionError):
    def __init__(self, txt):
        self.txt = txt


a = 1
b = 0

try:
    if b == 0:
        raise ZeroDivisionErr("На ноль делить нельзя!")
    c = a / b
except ZeroDivisionErr as err:
    print(err)
    print(f'c = {a} / {b} - невозможно вычислить')
