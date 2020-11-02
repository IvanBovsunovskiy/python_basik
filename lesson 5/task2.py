'''2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.'''
def del_odd_space(temp_string):
    while '  ' in temp_string:
        temp_string = temp_string.replace('  ', ' ')
    if temp_string[0] == ' ':
        temp_string = temp_string[1:]
    return temp_string


# open prepared text file and count number of lines and words in lines
with open('text2.txt', 'rt') as text_file:
    # read all lines
    # file_strings = text_file.readlines()

    # read line by line
    line_number = 0
    for file_string in text_file:
        line_number += 1
        # del new line symbol at the end of the string
        print(file_string[0:-1])
        file_string = del_odd_space(file_string)
        file_string = file_string.split(' ')
        print(f"String number - {line_number}, contain {len(file_string)} words separated by spaces\n")
