# write data to the end of the text file, each string on new line
user_string = 'test'
with open('text.txt', 'at') as text_file:
    while user_string != '':
        user_string = input("Please, enter string which you want to be added to the file"
                            "(note: empty string will end of adding data): ")
        text_file.write(user_string + '\n')
