"""
Задание 4. Написать программу, которая генерирует в указанных пользователем границах:
    случайное целое число;
    случайное вещественное число;
    случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

Подсказка:
Нужно обойтись без ф-ций randint() и uniform()
Использование этих ф-ций = задание не засчитывается

Функцию random() использовать можно
Опирайтесь на пример к уроку
"""
from random import random

m1 = int(input())
m2 = int(input())
n = int(random() * (m2 - m1 + 1)) + m1
print(n)

m1 = float(input())
m2 = float(input())
n = random() * (m2 - m1) + m1
print(round(n, 3))

m1 = ord(input())
m2 = ord(input())
n = int(random() * (m2 - m1 + 1)) + m1
print(chr(n))