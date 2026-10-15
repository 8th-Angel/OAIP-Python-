#Множества
#N1
print("Вывод N1")
a = {1,1,1,1,1,1}
print(a)
print(len(a))
#N2
print("Вывод N2")
a = {1,2,3}
a.add(4)
a.remove(3)
print(a)
#N3
print("Вывод N3")
a = {1,2,3}
b = {2,3,4,5}
print(a | b)
#N4
print("Вывод N4")
a = {1,2,3}
b = {2,3,4,5}
print(a & b)
#N5
print("Вывод N5")
a = {1,2,3}
b = {2,3,4,5}
print(a - b)
print(b - a)
#N6
print("Вывод N6")
a = {1,2,3}
b = {2,3,4,5}
print(a ^ b)
#N7
print("Вывод N7")
a = {1,2,3,4,5}
x = 1
if x in a:
    print(f"{x} есть в множестве")
else:
    print(f"{x} нет в множестве")
#N8
print("Вывод N8")
a = {1,2,3}
b = {2,3,4,5}
print(a <= b)
#N9
print("Вывод N9")
a = "телефон"
b = set(a)
print(b)
print(len(b))
#N10
print("Вывод N10")
a=[1,2,3,4]
b=[1,3,4,5]
a1=set(a)
b1=set(b)
print(a1 & b1)

#Кортежи
#N1
print("Вывод N1")
a = (1,2,3,4,5)
print(a[0])
print(a[-1])
print(a[len(a) // 2])
#N2
print("Вывод N2")
a=(1,2,3,4,5,6,7,8)
print(a[:2],a[-2:],a[::-1])
#N3
print("Вывод N3")
a=(1,2,3,4,5,6,7,8)
print(len(a), sum(a), min(a), max(a))
#N4
print("Вывод N4")
a=(1,2,3,1,5,6,7,8)
x = 1
print(x in a)
print(a.count(x))
print(a.index(x))

#N5
print("Вывод N5")
a=(1,2,3,4,5,6,7,8)
b=(7,8,9,10,11)
c = a+b
print(c)
#N6
print("Вывод N6")
a=(10)
print(type(a))
#N7
print("Вывод N7")
a = ("Борис",20,"Москва")
z,x,c = a
print(z,x,c)
#N8
print("Вывод N8")
a = 10
b = 12
(a,b) = (b,a)
print(a, b)
#N9
print("Вывод N9")
a=(1,2,3,4,5,6,7,8)
b=list(a)
b[1] = 111
a=tuple(b)
print(a)
#N10
print("Вывод N10")
a=(1,1,3,3,4,6,7,3)
a=set(a)
a=sorted(a)
a=tuple(a)
print(a)