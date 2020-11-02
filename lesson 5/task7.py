import json

def del_odd_space(temp_string):
    while '  ' in temp_string:
        temp_string = temp_string.replace('  ', ' ')
    if temp_string[0] == ' ':
        temp_string = temp_string[1:]
    return temp_string

new_comps_dict = {}
av_profit = []
with open('companies.txt', 'rt') as companies:
    for line in companies:
        line = del_odd_space(line)
        line = line.split(' ')
        try:
            profit = float(line[2]) - float(line[3])
        except ValueError:
            profit = 0
        finally:
            if profit > 0:
                if not av_profit:
                    av_profit = [profit,]
                else:
                    av_profit.append(profit)
        new_comps_dict.update({line[0]: profit})

av_profit = [x/len(av_profit) for x in av_profit]
res = 0
for item in av_profit:
    res += item
av_profit = res

profit_dict = {'average_profit': av_profit}

data = [new_comps_dict, profit_dict]

with open("companies_file.json", "w") as write_f:
    json.dump(data, write_f)
