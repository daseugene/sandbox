import time
from random import *
import math
def calculator_temperature():
    c = int(input("Введите температуру в градусах Цельсия: "))
    print(((c * (9/5))+32),"•F")


def chetnost():
    num = int(input("Введите число: "))
    if num % 2 == 0:
        print("Число четное")
    else:
        print("Число нечетное")

def discount_calc():
    price = int(input("Введите сумму: "))

    if price > 1000:
        price_calc = (price*10)/100
        print(price - price_calc)
    else:
        print("Скидка не предусмотрена")

def umnozhenie():
    n = int(input("Введите цифру: "))

    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

def max_number():
    print("Необходимо ввести три числа по порядку")
    a = [int(input()) for i in range(3)]
    print("Max num is: ",max(a))

def factorial_calc():
    n = int(input("Please input your number: "))
    counter = 1
    j = 1
    for i in range(1, n+1):
        j *= counter
        counter += 1
    print("Factorial is :", j)

def simple_num_check():
    n = int(input("Введите число: "))
    num_lst = []

    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                break
                print("Число не является простым")
        else:
            num_lst.append(i)
    print('Число простое')
def reverse_str():
    s = input()
    reversed_word = list(s)
    reversed_word.reverse()
    result = ''.join(reversed_word)
    print(result)

def palindrom_check():
    s = input("Введите строку: ")
    if s == s[::-1]:
        print("Палиндром найден - ", s)
    else:
        print("Не палиндром")


def random_number():
    print("Загадываю число...")
    time.sleep(3)
    a = randint(1, 100)
    n = int(input("Угадай число: "))

    while True:
        if n < a:
            print("Загаданное число больше")
            n = int(input("Продолжай пытаться угадать! - "))
        elif  n > a:
            print("Загаданное число меньше")
            n = int(input("Попытка - не пытка! - "))
        elif n == a:
            print("Ты победил!")
            break

while True:
    print("""
    1. Калькулятор температуры:
    2. Определение четности числа:
    3. Калькулятор скидки:
    4. Генератор таблицы умножения:
    5. Поиск максимального числа: 
    6. Калькулятор факториала:
    7. Проверка на простоту:
    8. Генератор случайных чисел:
    9. Обратный порядок строки:
    10. Проверка на палиндром:
    """)

    choose = input()

    if choose == "1":
        calculator_temperature()

    elif choose == "2":
        chetnost()

    elif choose == "3":
        discount_calc()

    elif choose == "4":
        umnozhenie()

    elif choose == "5":
        max_number()

    elif choose == "6":
        factorial_calc()

    elif choose == "7":
        simple_num_check()

    elif choose == "8":
        random_number()

    elif choose == "9":
        reverse_str()

    elif choose == "10":
        palindrom_check()

    elif choose == "0":
        break

    else:
        print("Выберите значение из представленного списка")
        continue