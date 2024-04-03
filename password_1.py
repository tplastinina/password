from random import *
from math import *

password = ''

def get_list_1():
    gen_list = 'abcdefghijklmnopqrstuvwxyz'
    return gen_list[randint(0,25)] 

def get_list_2():
    gen_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return gen_list[randint(0,25)]

def get_list_3():
    gen_list = '0123456789'
    return gen_list[randint(0,8)]

def get_list_4():
    gen_list = '!#$%&*+-=?@^_'
    return gen_list[randint(0,12)]

kol = int(input('Сколько паролей вам сегодня необходимо? '))
if int(kol) < 1:
     print('Минимально можем предложить один пароль')
     kol = input('Сколько паролей вам сегодня необходимо? ')


while int(kol) != 0:

    lange = input('Какой длинны пароль вам необходим? min = 6 ')

    while lange.isdigit() == False:
            print('Нужно вводить цифу. Попробуйте ещё раз:')
            lange = input('Какой длинны пароль вам необходим? ')

    if int(lange) < 6:
        print('Короче 6 пароли не генерируем')
        lange = input('Какой длинны пароль вам необходим? ')

    typ = input('Нужны ли (1)нижний регистр, (2)верхний регистр, (3)цифры, (4)специальные символы? ')

    while typ.isdigit() == False:
            print('Нужно вводить цифры. Попробуйте ещё раз:')
            typ = input('Нужны ли (1)нижний регистр, (2)верхний регистр, (3)цифры, (4)специальные символы? ')

    chars = ''

    for i in range(int(lange)):
        if "1" in typ:
            chars += str(get_list_1())
        if "2" in typ:
            chars += str(get_list_2())
        if "3" in typ:
            chars += str(get_list_3())
        if "4" in typ:
            chars += str(get_list_4())  

    for i in range(int(lange)):
        password += choice(chars)
        
    print(password) 
    password = '' 
    kol -= 1
