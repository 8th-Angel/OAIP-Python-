# N1
print("Вывод N1")
a = input('Введите слова в массив через пробел').split()
print(a[0], a[-1])
a[0],a[-1] = a[-1],a[0]
print(a[0], a[-1])
# N2
print("Вывод N2")
a = input('Введите слова в массив через пробел').split() #чётный
b = len(a) // 2
print(a[b])
print(a[b-1])
a = input('Введите слова в массив через пробел').split() #нечётный
b = len(a) // 2
print(a[b])
#N3
print("Вывод N3")
a = input('Введите слова в массив через пробел').split()
print(a[:3])
print(a[7:])
print(a[1::2])
print(a[::-1])
#N4
print("Вывод N4")
a = []
a.append(1)
a.append(2)
a.append(3)
a.insert(0,9)
a.pop()
print(a)
#N5
print("Вывод N5")
a = input('Введите слова в массив через пробел').split()
print(len(a))
print(sum(a))
print(min(a))
print(max(a))
print(sum(a) / len(a))
#N6
print("Вывод N6")
a = input('Введите слова в массив через пробел').split()
x = 1
if x in a:
    print(True)
    print(a.count(x))
    print(a.index(x))
else:
    print("Элемента в списке нет")
#N7
print("Вывод N7")
a = input('Введите слова в массив через пробел').split()
sort_a = sorted(a)
print(sort_a[:3])
print(sort_a[-3:])
#N8
print("Вывод N8")
a = input('Введите слова в массив через пробел').split()
b = input('Введите слова в массив через пробел').split()
c = a + b
c.sort(reverse=True)
print(c[1])
#N9
print("Вывод N9")
a = input('Введите строку ')
b = a.split()
b.sort()
c = ", ".join(b)
print(c)
#N10
print("Вывод N10")
a = input('Введите слова в массив через пробел').split()
k = int(input("Введите K "))
print(a[-k:] + a[:-k])