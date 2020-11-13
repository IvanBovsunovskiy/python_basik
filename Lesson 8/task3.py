class ListError(Exception):

    def __init__(self, txt):
        self.txt = txt
        # plus string 30
    '''def __init__(self):
        self.txt = 'You entered not a number'
        '''

    @staticmethod
    def is_number(input_string):
        try:
            float(input_string)
            return True
        except ValueError:
            return False


list_a = []
while True:
    user_string = input('Please enter list element, or stop to finish list filling.').lower()
    if 'stop' in user_string:
        break
    else:
        try:
            if ListError.is_number(user_string):
                list_a.append(float(user_string))
            else:
                raise ListError('You entered not a number')
                # raise ListError()
        except ListError as err:
            print(err)


print(f'sum of the list ({list_a}) elements is {sum(list_a)}')
