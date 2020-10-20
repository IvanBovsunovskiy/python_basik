# todo part 1
current_year = 2020
current_month = 10
S_current_month = 'october'
old_year = 2009
old_month = 7
if (current_month-old_month) > 0:
    print(f'Your experience {current_year-old_year} and {current_month-old_month}')
elif(current_month - old_month) < 0:
    print(f'Your experience {current_year - old_year - 1} and {12 + (current_month - old_month)}')
else:
    print(f'Your experience {current_year-old_year}')

# todo part 2
seconds = input('Please, enter time in seconds(only integer numbers allowed): ')
if seconds.isdigit():
    n_seconds = int(seconds)
    hours = n_seconds // 3600
    minutes = (n_seconds - hours*3600) // 60
    n_seconds = n_seconds - (hours * 60 + minutes) * 60
    if hours < 10:
        s_hours = ' 0' + str(hours)
    else:
        s_hours = ' ' + str(hours)
    if minutes < 10:
        s_minutes = '0' + str(minutes)
    else:
        s_minutes = str(minutes)
    if n_seconds < 10:
        s_seconds = '0' + str(n_seconds)
    else:
        s_seconds = str(n_seconds)

    print(f'Your entered time({seconds}) is equal to', s_hours, s_minutes, s_seconds, sep=':')
else:
    print("You entered wrong number")

# todo part 3
n = input('Please, enter numeral(only single numbers allowed): ')
if n.isdigit():
    if int(n) > 9:
        print('You entered number, not numeral.')
    else:
        n_n = int(n)
        print(f'Summ of n + nn + nnn = {(3 + 20 + 100)*n_n}')
else:
    print("You entered wrong numeral")

# todo part 4
s_n = input('Please, enter integer(only positive numbers allowed): ')
temp = 0
temp2 = 0
if s_n.isdigit():
    n = int(s_n)
    while n > 0:
        temp = n
        n = n // 10
        if n == 0:
            if temp > temp2:
                print(f'Max numeral in integer {s_n} is {temp}')
            else:
                print(f'Max numeral in integer {s_n} is {temp2}')
        else:
            temp2 = max(temp - n*10, temp2)

# todo part 5
s_proceeds = input('Please, enter company proceeds(only integer numbers): ')
s_costs = input('Please, enter company costs(only integer numbers): ')
if s_proceeds.isdigit() and s_costs.isdigit():
    proceeds = int(s_proceeds)
    costs = int(s_costs)
    if (proceeds - costs) > 0:
        print(f'Company works with profit = {proceeds - costs}')
        print(f'Company profitability = {(proceeds - costs) / proceeds}')
        s_number_of_emp = input('Please, enter number of employees: ')
        if s_number_of_emp.isdigit():
            print(f'Company profitability per employee = {(proceeds - costs) / proceeds / int(s_number_of_emp)}')
        else:
            print(f'Company profitability per employee undefined - number of employees is undefined!')
    else:
        print(f'Company is operating at a loss = {-proceeds + costs}')

# todo part 6
import math
s_a = input('Please, enter sportsmen path length in km per first day: ')
eval_percent = 1.1
s_b = input('Please, enter overall sportsmen path length in km: ')
if s_a.isdigit() and s_b.isdigit():
    a = int(s_a)
    b = int(s_b)
    # из суммы геометрической прогрессии имеем
    n = math.log((1 - b * (1 - eval_percent) / a), eval_percent)
    if n == math.ceil(n):
        n += 1
    else:
        n = math.ceil(n)
    print(f'Sportsmen will run more then {b}km on {n}day')
else:
    print("You entered wrong numeral")
