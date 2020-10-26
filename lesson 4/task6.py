class IntegerIterator:
    """first arg - start, second number of counts. in case of second number = 0 sys.maxsize will be used - max integer
    value for current system"""
    def __iter__(self):
        return self

    def __init__(self, *data):
        from sys import maxsize
        if not len(data):
            self.start = 1
            self.limit = 10
        elif len(data) == 1:
            self.start = data[0]
            self.limit = 10
        elif len(data) >= 2:
            self.start = data[0]
            if data[1] == 0:
                self.limit = maxsize
            else:
                self.limit = data[1]
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter + self.start - 1
        else:
            raise StopIteration

print('First script - integers cycle')
s_iter2 = IntegerIterator(3, 7)
for i in s_iter2:
    print(i)


'''second part___--------------------------------------------------------------------------------------------------'''
print('Second script list cycle')
import itertools
temp_list = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
a = itertools.cycle(temp_list)
count = 1
while count <= 22:
    count += 1
    print(next(a))
