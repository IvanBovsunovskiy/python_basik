def del_odd_space(temp_string):
    while '  ' in temp_string:
        temp_string = temp_string.replace('  ', ' ')
    if temp_string[0] == ' ':
        temp_string = temp_string[1:]
    return temp_string


def list_sum(*args):
    temp_result = 0
    args = args[0]
    for item in args:
        temp_result += item
    return temp_result


average_salary = []
low_sal_persons = []
with open('salary.txt') as salary_file:
    for person in salary_file:
        person = del_odd_space(person)
        person_data = person.split(' ')
        try:
            salary = float(person_data[1])
        except ImportError:
            print('err')
        if salary < 20:
            low_sal_persons.append(person_data[0])
        average_salary.append(salary)
print(f'Emploeyrs {", ".join(low_sal_persons)} have salaries lowe then 20')
print(f'Average salary is {list_sum(average_salary)/len(average_salary)}')


