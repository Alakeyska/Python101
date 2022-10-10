# Даны два числа n и m. Создайте двумерный массив размером
# n×m и заполните его символами "." и "*" в шахматном порядке. В
# левом верхнем углу должна стоять точка.


import numpy
n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))
shape = (n, m)
a=numpy.zeros(shape)
for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0:
            a[i][j]=1
        else:
            a[i][j]=0
print(a)


