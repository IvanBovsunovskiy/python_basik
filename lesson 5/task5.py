import random

ind = 1
with open('numbers.txt', 'w') as numbers:
    while ind <= 5:
        numbers.write(str(random.uniform(0, 10)) + ' ')
        ind += 1
with open('numbers.txt', 'r') as numbers:
    result = 0
    data = numbers.readlines()
    data = data[0].split(' ')
    for item in data:
        try:
            temp = float(item)
        except ValueError:
            temp = 0
        finally:
            result += temp
            #print(result)

print(result)
