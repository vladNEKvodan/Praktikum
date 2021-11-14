import os
import shutil
from settings import *

print("Файловый менеджер: \n"
      "1.Создать папку \n"
      "2.Удалить папку \n"
      "3.Переместиться \n"
      "4.Вернуться в рабочую директорию \n"
      "5.Создать текстовый файл \n"
      "6.Записать текст в файл \n"
      "7.Посмотреть содержимое файла \n"
      "8.Удалить файл \n"
      "9.Скопировать файл в другую папку \n"
      "10.Переместить файл \n"
      "11.Переименовать файл \n"
      "12.Содержимое папки \n"
      "13.Вернуться назад")

request = ''


def create():
    name = input('Название папки:')
    new_path = os.getcwd() + os.sep + name
    os.mkdir(new_path)
    print('Готово!')


def deleting():
    try:
        name = input('Папка: ')
        dir_for_del = os.path.dirname(os.getcwd())
        dirrr = os.getcwd() + os.sep + name
        os.rmdir(dirrr)
    except OSError:
        askk = input("Вы уверены, что хотите удалить папку?: ")
        if askk == 'да':
            shutil.rmtree(dirrr)
            print("Готово!")
        else:
            os.chdir(dir_for_del)
            print(os.getcwd())


def walking():
    namme = input('Куда: ')
    new_dir = os.getcwd() + os.sep + namme
    os.chdir(new_dir)
    print(os.getcwd())


def backhome():
    global working_path
    os.chdir(working_path)
    print(os.getcwd())


def spisok():
    print(os.listdir(os.getcwd()))


def sozdat():
    name = input('Имя файла:')
    open(name, 'w')
    print('Файл создан в: ' + os.getcwd())


def writing():
    name = str(input('Файл: '))
    f = open(name, 'w')
    f.write(input())
    f.close()


def reading():
    name = str(input('Файл: '))
    f = open(name)
    print(f.read())


def udaling():
    name = input('Файл: ')
    os.remove(name)
    print("Готово!")



def copying():
    global working_path
    name = input('Файл: ')
    ppapka = input("Папка, в которую копируем: ")
    shutil.copy(os.getcwd() + os.sep + name, working_path + os.sep + ppapka)
    print('Скопировано!')


def replacing():
    global working_path
    naming = input('Файл: ')
    ppapkka = input("Папка, в которую перемещаем: ")
    os.replace(os.getcwd() + os.sep + naming, working_path + os.sep + ppapkka + os.sep + naming)
    print('Перемещено!')


def renaming():
    naming = input('Файл: ')
    new_name = input('Введите новое название: ')
    os.rename(os.getcwd() + os.sep + naming, os.getcwd() + os.sep + new_name)
    print('Переименовано')


while request != 'end':
    request = input()

    if request == "1":
        create()

    elif request == "2":
        deleting()

    elif request == "3":
        walking()

    elif request == "4":
        backhome()

    elif request == "5":
        sozdat()

    elif request == "6":
        writing()

    elif request == "7":
        reading()

    elif request == "8":
        udaling()

    elif request == "9":
        copying()

    elif request == "10":
        replacing()

    elif request == "11":
        renaming()

    elif request == "12":
        spisok()

    elif request == "13":
        backwk()


