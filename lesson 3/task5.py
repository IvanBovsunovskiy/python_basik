def sum_of_elements(list_of_numbers):
    num_s = 0
    for num in list_of_numbers:
        num_s = num_s + num
    return num_s


result = 0
check = True
while check:
    user_numbers = []
    user_str = (input('Please, enter numbers separated by single space or Q to stop calculations: ').split(' '))
    for item in user_str:
        if item != '':
            try:
                user_numbers.append(float(item))
            except ValueError:
                if item == 'Q':
                    result = result + sum_of_elements(user_numbers)
                    print(f'Sum of numbers is - {result}')
                    check = False
    if check:
        result = result + sum_of_elements(user_numbers)
        print(f'Sum of numbers is - {result}')
