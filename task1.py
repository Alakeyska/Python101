# Пользователь вводит натуральное число. Определить, будет ли это число: чётным, кратным 5, результат вывести.


a = int(input('enter your number: '))
if a % 2 == 0 and a % 5 == 0:
    print('число %d четное и кратное пяти' % a)
elif a % 2 == 0:
    print('число %d четное' % a)
elif a % 5 == 0:
    print('число %d кратное пяти' % a)
else:
    print('число %d не подходит ни к одному из критериев' % a)