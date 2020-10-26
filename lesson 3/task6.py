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
