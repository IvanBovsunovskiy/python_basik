def check_repetition(*args):
    """check_repetition - generator, get list of elements and return item from list in case of single quantity"""
    for item in args:
        if args.count(item) == 1:
            yield item


a = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
b = [item for item in check_repetition(*a)]
print(b)
