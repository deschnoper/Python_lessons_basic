
__author__ = 'Гурьянов Андрей Юрьевич'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

import math

a = input ('Введите целое число: ')
b=0
i=0
while i < len(a):
    if int(a[i],10)>b:
        b = int(a[i],10)
    i += 1
print('Маскимальная цифра в данном числе: ',b)

a = input ('Введите другое целое число: ')
b = 0
for i in a:
    if int(i,10)>b:
        b = int(i,10)
print('Маскимальная цифра в данном числе: ',b)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

print('\nРешение через действия над числами\n')
a = int(input('Введите значение первой переменной: '))
b = int(input('Введите значение второй переменной: '))
b = a+b
a = b-a
b = b-a
print('Первая переменная: ',a)
print('Вторая переменная: ',b)

print('\nРешение с помощью кортежей\n')
a = tuple(input('Введите значение первой переменной: '))
b = tuple(input('Введите значение второй переменной: '))
b = a+b
a = b[len(a):]
b = b[:len(a)]  # Похоже, в переменную b записывается больше значений, чем нужно, если длина переменной a меньше, чем b. Ер я не пойму, почему...
                # работает только если обе введённые строки a и b одинаковой длины
new_a = ''
for x in a:
    new_a = new_a + x
a = int(new_a)

new_b = ''
for x in b:
    new_b = new_b + x
b = int(new_b)

print('Первая переменная: ',a)
print('Вторая переменная: ',b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

print('\nВычисление квадратного уравнения вида ax2 + bx + c = 0\n')
a = int(input('Введите значение a: '))
b = int(input('Введите значение b: '))
c = int(input('Введите значение c: '))
D = b**2 - 4*a*c
if D<0:
    print('Корней нет')
elif D == 0:
    x = (-b + math.sqrt(D)) / (2*a)
    print('Корень один: x = ',x)
else:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print('Корней два:')
    print('x1 = ',x1)
    print('x2 = ', x2)
