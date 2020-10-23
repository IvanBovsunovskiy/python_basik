def two_numbers_div(a, b):
    try:
        return print(f'Результат деления числа {a} на число {b} = {a / b}')
    except ZeroDivisionError:
        print(f'You entered b = {b}.')


x = []
while True:
    numbers_str = input('Please, enter two numbers separated by comma: ')
    if len(numbers_str) > 0:
        numbers_str = numbers_str.split(',')
        break
    else:
        print('You entered empty string.')

check = True
for item in numbers_str:
    if item != '':
        try:
            x.append(float(item))
        except ValueError:
            if check:
                print('One of the entered values is not a number.')
                check = False
if len(x) == 0:
    print('You did not enter any numbers.')
elif len(x) == 1:
    print(f'You entered only one number {x} which will be divided by itself.')
    two_numbers_div(x[0], x[0])
elif len(x) == 2:
    two_numbers_div(x[0], x[1])
else:
    print(f'You entered more then two numbers ({len(x)}). Only first two will be used.')
    two_numbers_div(x[0], x[1])
