def my_func(x,y):
    temp = 1
    ind = 1
    while ind <= -y:
        temp = temp/x
        ind += 1
    return temp


print(my_func(2, -2))
