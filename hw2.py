# todo 1.
list_1 = [1, 3, 1.5, 'text']
for item in list_1:
    print(type(item))
print(f'Type of {list_1[1]+1} element is {type(list_1[list_1[1]])}')

# todo 2.
list_1 = []
while True:
    temp = input('Please, enter new list element or q for exit: ')
    if temp.isdigit():
        temp = int(temp)
    list_1.append(temp)
    if list_1[-1] == 'q':
        list_1.remove('q')
        break
print('Initial list of elements: ', list_1)
temp = len(list_1) // 2
index = 0
while index < temp:
    # not include last element
    a, b = list_1[index*2 : index*2 + 1 + 1]
    list_1[index * 2: index * 2 + 1 + 1] = b, a
    index += 1
print('Resorted list of elements: ', list_1)

# todo 3. Напишите решения через list и через dict.
#list
season_list = ['winter','winter','spring','spring','spring','summer','summer','summer','autumn','autumn','autumn',
               'winter']
temp = ''
while True:
    temp = input('Please, enter month number (1-12, or q - for exit, ''list method''): ')
    if temp.isdigit():
        temp = int(temp)
        if (temp > 0) and (temp <13):
            print('Entered month number corresponds to the ', season_list[int(temp) - 1])
            break
    elif temp == 'q':
        break
#dict
season_dict = {'12':'winter', '1':'winter', '2':'winter', '3':'spring', '4':'spring', '5':'spring', '6':'summer',
               '7':'summer', '8':'summer', '9':'autumn', '10':'autumn', '11':'autumn'}
while True:
    temp = input('Please, enter month number (1-12, or q - for exit, ''dict method''): ')
    if not(temp in season_dict.keys()):
        if temp == 'q':
            break
    else:
        print('The month number corresponds to the ', season_dict[temp])
        break

# todo 4.
temp = input('Please, enter string consist of few words, or q - for exit): ')
list_1 = temp.split(' ')
index_string = 0;
for temp in list_1:
    if temp != '':
        index_string += 1
        print(f'Word number {index_string} in entered string is ', temp[0:10])

# todo 5
list_1 = [7, 5, 3, 3, 2]
while True:
    temp = input('Please, enter natural number, or q - for exit: ')
    if temp.isdigit():
        temp = int(temp)
        if temp in list_1:
            list_1.insert(list_1.index(temp)+list_1.count(temp), temp)
        else:
            for list_item in list_1:
                # if to avoid looping
                if not(temp in list_1):
                    if temp > list_item:
                        list_1.insert(list_1.index(list_item), temp)
# or break
                    elif (temp < list_item) and (list_1.index(list_item) + 1) == len(list_1):
                        list_1.insert(list_1.index(list_item)+1, temp)

    elif  temp == 'q':
        break
print(list_1)

# todo 6
goods = []
temp = 0
while True:
    temp_name = input('Please, product name,  or q - for exit: ')
    if temp_name == 'q':
        break
    temp_price = input('Please, product price: ')
    if temp_price.isdigit():
        temp_price = int(temp_price)
    temp_quantity = input('Please, product quantity: ')
    if temp_quantity.isdigit():
        temp_quantity = int(temp_quantity)
    temp_unit = input('Please, product unit:')
    temp_struct = [1, {'name': temp_name, 'price': temp_price, 'quantity': temp_quantity, 'unit': temp_unit}]
    goods.append(temp_struct)
    temp += 1
temp = 0
name_arr = []
price_arr = []
quantity_arr = []
unit_arr = []
while temp < len(goods):
    q, item = goods[temp]
    temp += 1
    name_arr.append(item['name'])
    price_arr.append(item['price'])
    quantity_arr.append(item['quantity'])
    unit_arr.append(item['unit'])
goods_dict = {'name':name_arr, 'price':price_arr, 'quantity':quantity_arr, 'unit':unit_arr}
print(goods_dict)
