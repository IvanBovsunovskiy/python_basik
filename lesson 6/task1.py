import time
'''Для того, чтобы код, написанный с помощью внутренних средств Python 3 или с помощью библиотеки termcolor заработал 
в Windows 10, надо включить поддержку ANSI для stdout в запущенной консоле. пока не протестировано для windows. 
in windows uncomment next lines'''
# import ctypes
# kernel32 = ctypes.windll.kernel32
# kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)


class TrafficLight:
    __color = None

    def __init__(self):
        self.__color = 1

    def running(self):
        """changing of traffic light on - background color. Colors could be changed only in the following order:
        red - orange - green - orange - red """
        if self.__color % 2 == 0:
            print("\033[30m \033[43m {}".format('Orange'))
            time.sleep(2)
            print("\033[0m {}".format(''))
        elif (self.__color - 3) % 4 == 0:
            print("\033[30m \033[42m {}".format('Green'))
            time.sleep(3)
            print("\033[0m {}".format(''))
        else:
            print("\033[30m \033[41m {}".format('Red'))
            time.sleep(7)
            print("\033[0m {}".format(''))
        self.__color += 1


traffic_color = TrafficLight()
item = 1
while item <= 6:
    traffic_color.running()
    item += 1
