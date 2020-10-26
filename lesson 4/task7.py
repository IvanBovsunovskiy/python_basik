def my_fact(*args):
    """my_fact calculate factorial using first arg"""
    '''later will be changed to return factorial for list'''
    temp = 1
    global counter
    counter = 1
    if not len(args):
        return []
    else:
        while True:
            if counter <= args[0]:
                yield temp
                counter += 1
                temp *= counter
            else:
                break


counter = 1
for i in my_fact(5):
    print(f'factorial {counter}! = ', i)
