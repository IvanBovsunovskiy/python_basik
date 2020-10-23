'''6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно
начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().'''
def int_func(text):
    if len(text) == 1:
        return text.title()
    elif len(text) == '':
        return text
    else:
        temp = text[0]
        temp = temp.title() # capitalize()
        return temp + text[1:]


str_text = 'wefr qwe, ewr ,ert e qwe Qergw wE'
str_text = str_text.split()
for item in str_text:
    str_text[str_text.index(item)] = int_func(item)
str_text = ' '.join(str_text)
print(str_text)
