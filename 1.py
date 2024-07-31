# Напишите программу, которая получает целое число
# и возвращает его шестнадцатеричное строковое
# представление. Функцию hex используйте для проверки
# своего результата.
DIV_HEX = 16
F = 15
E = 14
D = 13
C = 12
B = 11
A = 10

num = int(input('введите целое число: '))
rez2 = hex(num)
print(f'через функцию hex: {rez2}')


result: str = ''
while num > 0:
    digit = num % DIV_HEX
    if digit < 10:
        result = str(num % DIV_HEX) + result
        num = num // DIV_HEX
    elif digit == A:
        result = str('A') + result
        num = num // DIV_HEX
    elif digit == B:
        result = str('B') + result
        num = num // DIV_HEX
    elif digit == C:
        result = str('C') + result
        num = num // DIV_HEX
    elif digit == D:
        result = str('D') + result
        num = num // DIV_HEX
    elif digit == E:
        result = str('E') + result
        num = num // DIV_HEX
    elif digit == F:
        result = 'f' + result
        num = num // DIV_HEX




print(f'ручной подсчет: 0х{result}')
