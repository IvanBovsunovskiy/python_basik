
def current_user(user_name = 'User name', user_surname = 'User surname', user_birth_date = 'none', user_location = 'none',
                 user_email = 'none@none.none', user_phone = 'none', ):
    print('Your entered the following user data:',
          f'User name - {user_name}, User surname - {user_surname}, User date of birth -  {user_birth_date},' 
          f'User city - {user_location}, User email -  {user_email}, User phone - {user_phone}', sep='\n')


while True:
    user_str = (input('Please, enter user data separated by comma(Name, Surname, birth date, city, email, phone): ')
                .split(','))
    if ('' in user_str) and (len(user_str) == 1):
        print('You entered empty string. Please retry to enter user data')
    else:
        break

while '' in user_str:
    user_str.remove('')


if len(user_str) == 0:
    print('You entered empty string. Please retry to enter user data')
    current_user()
elif len(user_str) == 1:
    current_user(user_name=user_str[0],)
elif len(user_str) == 2:
    current_user(user_name=user_str[0], user_surname=user_str[1],)
elif len(user_str) == 3:
    current_user(user_name=user_str[0], user_surname=user_str[1], user_birth_date=user_str[2],)
elif len(user_str) == 4:
    current_user(user_name=user_str[0], user_surname=user_str[1], user_birth_date=user_str[2], user_location=user_str[3],)
elif len(user_str) == 5:
    current_user(user_name=user_str[0], user_surname=user_str[1], user_birth_date=user_str[2], user_location=user_str[3],
                 user_email=user_str[4],)
elif len(user_str) == 6:
    current_user(user_name=user_str[0], user_surname=user_str[1], user_birth_date=user_str[2], user_location=user_str[3],
                 user_email=user_str[4], user_phone=user_str[5])
elif len(user_str) > 6:
    print('You entered more user data then was requested. Only first 6 will be used.')
    current_user(user_name=user_str[0], user_surname=user_str[1], user_birth_date=user_str[2],
                 user_location=user_str[3], user_email=user_str[4], user_phone=user_str[5])
