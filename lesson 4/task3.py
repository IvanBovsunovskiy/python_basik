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



def my_min(*args):
    """my_min search/return min value in args"""
    if not len(args):
        return []
    else:
        min_value = args[0]
        for item in args:
            if item <= min_value:
                min_value = item
    return min_value


def my_max(*args):
    """my_max search/return max value in args"""
    if not len(args):
        return []
    else:
        max_value = args[0]
        for item in args:
            if item >= max_value:
                max_value = item
    return max_value


def my_sorted(*args):
    """my_sorted works only with args. used args(list) and returned sorted from min to max list"""
    args = list(args)
    # не понял как передать не tuple в функцию
    if not len(args):
        return []
    elif len(args) == 1:
        return args[0]
    else:
        shifted_first = 1
        end = len(args)
        while True:
            min_val = my_min(*args[shifted_first - 1: end])
            min_pos = args.index(min_val, shifted_first - 1, end)
            if not (min_pos == shifted_first - 1):
                args[shifted_first - 1], args[min_pos] = \
                    args[min_pos], args[shifted_first - 1]
            shifted_first += 1
            if shifted_first == end:
                break
        return args


print(my_sorted(*(list(my_range(20, 240, 20)) + list(my_range(21, 240, 21)))))
