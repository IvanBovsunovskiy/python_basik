# to avoid import path problems just copied from task 3
# from task3 import my_range
def my_range(*args):
    """my_range get *args (start, stop, step) and return value x = start + step * (iteration_number - 1)
    iteration_number is integer."""
    start = 0
    stop = 0
    step = 1
    my_list = []
    iteration = 1
    check = True
    while check: # не забывать про цикл, а то опять 3 часа потеряешь
        if not len(args):
            return []
        elif len(args) == 1:
            if args[0] == 0:
                return []
            elif args[0] > 0:
                stop = args[0]
        elif len(args) == 2:
            if args[0] >= args[1]:
                return []
            else:
                start = args[0]
                stop = args[1]
        elif len(args) >= 3:
            if args[0] == args[1]:
                return []
            elif args[2] == 0:
                return []
            elif ((args[0] >= args[1]) and (args[2] < 0)) or ((args[0] <= args[1]) and (args[2] > 0)):
                start = args[0]
                stop = args[1]
                step = args[2]
            else:
                return []
        current = start + (iteration - 1) * step
        if (current >= stop and args[2] > 0) or (current <= stop and args[2] < 0):
            current = []
            check = False
        else:
            yield current
        iteration += 1


'''
#without list
result1 = 1
for item in my_range(100, 1000+1, 2):
    result1 *= item
print(result1)
'''
prepared_list = list(my_range(100, 1000+1, 2))
print(f'There are first - {prepared_list[0]} and last - {prepared_list[-1]} elements in list')
check = True
result = 1
while check:
    try:
        result *= prepared_list.pop()
    except IndexError:
        check = False
print(result)
