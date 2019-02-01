# [Андрей Гурьянов]

# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random
print('\n\nЗадача 1\n')
rand_list = [random.randint(1,100) for _ in range(10)]
modif_list = [el**2 for el in rand_list]
print('Исходный список: ',rand_list)
print('Модифицированный список: ',modif_list)




# Задание-2:

print('\n\nЗадача 2\n')

# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits_1 = ['яблоко', 'апельсин', 'дыня', 'арбуз', 'персик', 'банан', 'ананас', 'манго', 'груша', 'гррейпфрут']
fruits_2 = ['абрикос', 'яблоко', 'лайм', 'лимон', 'банан', 'груша', 'дыня', 'папайя', 'авокадо', 'гранат', 'персик']
if len(fruits_1) > len(fruits_2):
    fruits_list = [el for el in fruits_1 if el in fruits_2]
else:
    fruits_list = [el for el in fruits_2 if el in fruits_1]
print('Список фруктов 1: ', fruits_1)
print('Список фруктов 2: ', fruits_2)
print('Список фруктов, которые есть в обоих списках: ', fruits_list)


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

print('\n\nЗадача 2\n')
rand_lst = [random.randint(-100,100) for _ in range(10)]
new_lst = [el for el in rand_lst if (el % 3 == 0) and (el > 0) and (el % 4 != 0)]
print('Список 1: ', rand_lst)
print('Список по условиям: ', new_lst)

