import datetime


class Data:
    data_string = None
    date = []

    def __init__(self, data_string: str):
        if data_string.count('-') != 2:
            print('String with date used for object initialization is in wrong format, will be used current date.')
            self.data_string = f'{datetime.datetime.today().day}-{datetime.datetime.today().month}-' \
                               f'{datetime.datetime.today().year}'
        else:
            self.data_string = data_string

    @classmethod
    def date_to_number(cls, data_string):
        cls.date = list(map(int, data_string.split('-')))

    @staticmethod
    def check_date(checking_date):
        """return False if date is incorrect and True if date is correct"""
        date_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        check = False
        if checking_date[2] % 400 == 0:
            leap_year = True
        elif checking_date[2] % 100 == 0:
            leap_year = False
        elif checking_date[2] % 4 == 0:
            leap_year = True
        else:
            leap_year = False
        if checking_date[1] in range(13):
            check = True
            if not (checking_date[0] in range(date_dict.get(checking_date[1]) + 1)
                    or (leap_year and checking_date[1] == 2 and checking_date[0] == 29)):
                check = False
        return check


a = Data('29-02-2019')
print(a.data_string)
a.date_to_number(a.data_string)
print(a.date)
print(a.check_date(a.date))


b = Data('29-02-2020')
print(b.data_string)
b.date_to_number(b.data_string)
print(b.date)
print(b.check_date(b.date))
