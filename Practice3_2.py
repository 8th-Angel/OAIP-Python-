#N1
print('Вывод N1')
a = input('Введите строку ')
print(len(a), a[0], a[-1])
#N2
print('Вывод N2')
a = input('Введите строку ') # чётный
b = len(a) // 2
print(a[b])
print(a[b-1])
a = input('Введите строку ') # нечётный
b = len(a) // 2
print(a[b])
#N3
print('Вывод N3')
a = input('Введите строку ')
print(a[:3])
print(a[-3:])
print(a[1::2])
print(a[::-1])
#N4
print('Вывод N4')
a = input('Введите строку ')
print(a.upper())
print(a.lower())
print(a.capitalize())
#N5
print('Вывод N5')
a = input('Введите строку ')
c = 'i'
if c in a:
    print("символ есть в строке ")
    print(a.count(c))
    print(a.index(c))
else:
    print("символа нет ")
#N6
print('Вывод N6')
a = input('Введите строку ')
print(a.replace(" ", "_"))
#N7
print('Вывод N7')
a = input('Введите строку ')
print(a.rstrip().lstrip())
#N8
print('Вывод N8')
a = input('Введите строку ')
b, c = a.split()
print(b)
print(c)
print(b[0], c[0])
#N9
print('Вывод N9')
a = input('Введите строку ')
b = a.lower()
if b == b[::-1]:
    print('Это палиндромон')
else:
    print("Это не палиндромон")
#N10
print('Вывод N10')
a = input('Введите строку ')
b = a.split()
print(len(b))
print(b[0])
print(b[-1])
