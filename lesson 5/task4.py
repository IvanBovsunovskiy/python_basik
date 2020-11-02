'''4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.'''
new_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
            'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
new_lines = []
with open('task_4.txt', 'rt') as f_read:
    for line in f_read:
        line = line.split(' ')
        line[0] = new_dict[line[0].lower()]
        new_lines.append(' '.join(line))

# symbol new line already in data
new_lines = ''.join(new_lines)

with open('task_4_new.txt', 'wt') as f_write:
    f_write.write(new_lines)
