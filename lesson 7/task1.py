class Matrix:
    """class Matrix get array(list of list) in init state and save it in Matrix.array.
    For better displaying by print used redefined function __str__ which shows
    elements of 2d array separated by |, and each string begins from new line.
    Redefined function __add__ can summarize Matrix.array with numbers, lists and Matrix.arrays element by element
    (begins from the 1 element in first line).
    if added array(list of list) have bigger size final matrix will have maximum size(in rows and columns)"""
    array = []
    __temp_i_range = None
    __str_array_length = None
    __str_other_length = None

    def __init__(self, array):
        self.array = array

    def __str__(self):
        string_view = ''
        if isinstance(self.array, list):
            for item in self.array:
                if isinstance(item, list):
                    string_view = string_view + ' | '.join(map(str, item)) + f'\n'
                else:
                    string_view = string_view + ' | ' + str(item) + ' | ' + f'\n'
        else:
            string_view = str(self.array)
        return string_view

    @staticmethod
    def arrays_sum(list_1, list_2):
        temp_length_max = len(list_1)
        temp_length_min = len(list_2)
        if temp_length_max < temp_length_min:
            [list_1, list_2] = [list_2, list_1]
            temp_length_min = temp_length_max
        for i in range(temp_length_min):
            list_1[i] += list_2[i]
        return list_1

    def __add__(self, other):
        if isinstance(other, Matrix):
            other = other.array
            if len(other) == 1 and isinstance(other, list):
                other = other[0]
        try:
            self.__str_array_length = len(self.array)
        except TypeError:
            try:
                self.__str_other_length = len(other)
                if isinstance(other[0], list):
                    other[0][0] += self.array
                else:
                    other[0] += self.array
                self.array = other
                return self.array
            except TypeError:
                return self.array + other
        try:
            self.__str_other_length = len(other)
        except TypeError:
            if isinstance(self.array[0], list):
                self.array[0][0] = self.array[0][0] + other
            else:
                self.array[0] = self.array[0] + other
            return self
        if (not isinstance(self.array[0], list)) and (not isinstance(other[0], list)):
            self.array = self.arrays_sum(self.array, other)
            return self
        elif (isinstance(self.array[0], list)) and (not isinstance(other[0], list)):
            self.array[0] = self.arrays_sum(self.array[0], other)
            return self
        elif (not isinstance(self.array[0], list)) and (isinstance(other[0], list)):
            [self.array, other] = [other, self.array]
            self.array[0] = self.arrays_sum(self.array[0], other)
            return self
        else:
            if self.__str_array_length < self.__str_other_length:
                [self.__str_array_length, self.__str_other_length] = \
                    [self.__str_other_length, self.__str_array_length]
                [self.array, other] = [other, self.array]
            for i in range(self.__str_other_length):
                self.array[i] = self.arrays_sum(self.array[i], other[i])
            return self


a = Matrix([[1, 2, 3], [4, 5, 6, 7, 8]])
print('a = ')
print(a)
b = Matrix([1])
print('b = ')
print(b)
a = a + b
print('a = a + b = ')
print(a)
c = Matrix([1, -2, -3])
print('c = ')
print(c)
a = c + a
print('a = c + a = ')
print(a)
d = Matrix([[1, 0, 0, 1], [0, 1], [1, 2]])
print('d = ')
print(d)
a = d + a
print('a = d + a = ')
print(a)
a = a + [1, 2, 3, 4, 5, 6]
print('a + [1, 2, 3, 4, 5, 6] = ')
print(a)
