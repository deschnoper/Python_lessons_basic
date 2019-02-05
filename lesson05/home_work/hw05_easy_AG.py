# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil

# Функции для задания Normal
def dir_change(dir_name):
    dir_path = os.path.join(os.getcwd(),dir_name)
    try:
        os.chdir(dir_path)
        return True
    except FileNotFoundError:
        return False

def list_curr_dir():
    dir_path = os.getcwd()
    try:
        print(os.listdir(dir_path))
        return True
    except FileNotFoundError:
        return False

def create_dir(dir_name):
    dir_path = os.path.join(os.getcwd(),dir_name)
    try:
        os.mkdir(dir_path)
        return True
    except FileExistsError:
        return False

def delete_dir(dir_name):
    dir_path = os.path.join(os.getcwd(),dir_name)
    try:
        os.rmdir(dir_path)
        return True
    except FileNotFoundError:
        return False

def user_choice():
    print('Выберите действие:')
    print('1. Перейти в папку')
    print('2. Просмотреть содержимое текущей папки')
    print('3. Удалить папку')
    print('4. Создать папку')
    while True:
        result = input('Введите номер Вашего ответа: ')
        try:
            result = int(result)
        except ValueError:
            continue
        if result in range(1,5):
            return int(result)


print('\n\nЗадача 1\n')
# Script 1
for num in range(1,10):
    dir_name = 'dir_' + str(num)
    dir_path = os.path.join(os.getcwd(),dir_name)
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Директория ', dir_name, ' уже существует')

#Script 2     
for num in range(1,10):
    dir_name = 'dir_' + str(num)
    dir_path = os.path.join(os.getcwd(),dir_name)
    try:
        os.rmdir(dir_path)
    except FileNotFoundError:
        print('Директория ', dir_name, ' не существует')



# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

print('\n\nЗадача 2\n')
#Для выводов результа, если в текущей директории нет папок, необходимо
#закомментировать Script 2 из Задачи 1
list_dir = os.listdir(os.getcwd())
for name in list_dir:
    if os.path.isdir(name):
        print(name)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

print('\n\nЗадача 3\n')

#Не нашёл как определить имя файла, из которого запускается скрипт. 
#shutil.copyfile()






