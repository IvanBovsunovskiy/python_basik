def bigger_then_previous(*temp_list):
    """bigger_then_previous - Function(object)
     get list and return items which is bigger then previous elements in list
     for each function call, changes global variable previous_element on current list
    item value to compare it on next call with next item in list"""
    global previous_element
    for item in temp_list:
        if not temp_list.index(item):
            previous_element = item
        else:
            if item > previous_element:
                yield item
            previous_element = item


a = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
b = []
previous_element = []
for item_b in bigger_then_previous(*a):
    b.append(item_b)
print(b)
