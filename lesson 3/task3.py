def my_func(a,b,c):
    if (a <= b and a < c) or (a < b and a <= c):
        return b + c
    elif (b <= a and b < c) or (b < a and b <= c):
        return a + c
    elif (c <= a and c < b) or (c < a and c <= b):
        return a + b


print(my_func(3,0.5,1))
