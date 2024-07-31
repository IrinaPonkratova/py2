# Напишите программу, которая принимает две строки
# вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions

from fractions import Fraction


a = input('введите первую строку вида “a/b”: ').split('/')
b = input('введите вторую строку вида “a/b”: ').split('/')
print(a)
print(b)

p1 = int(a[0]) * int(b[0])
p2 = int(a[1]) * int(b[1])
print(f'произведение дробей: {p1} / {p2}')

if a[1] != b[1]:
    znam = int(a[1]) * int(b[1])
    a[0] = (int(znam) / int(a[1])) * int(a[0])

    b[0] = (int(znam) / int(b[1])) * int(b[0])

    s1 = int(a[0]) + int(b[0])
else:
    s1 = int(a[0]) + int(b[0])
    znam = a[1]
print(f'сумма дробей: {s1} / {znam}')



f1 = Fraction(4, 5)  # Создает дробь 3/4
f2 = Fraction(1, 10)  # Создает дробь 1/2

print(f'сумма: {f1 + f2}')
print(f'произведение: {f1 * f2}')

