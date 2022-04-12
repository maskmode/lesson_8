class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('Введите значение и нажмийте Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - введите число")
                yorn = input(f'Попробовать еще раз? Y/N ')

                if yorn == 'Y' or yorn == 'y':
                    print(try_except.my_input())
                elif yorn == 'N' or yorn == 'n':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'


try_except = Error(1)
print(try_except.my_input())

