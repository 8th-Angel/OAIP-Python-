import random
# #for
# #N1
print("Вывод N 1")
for i in range(1,11):
    print(i)
#N2
print("Вывод N 2")
for i in range(2,51,2):
    print(i)
#N3
print("Вывод N 3")
for i in range(10,1,-1):
    print(i)
#N4
print("Вывод N 4")
n = int(input("Введите число "))
sum = 0
for i in range(1,n):
    sum+=n
print(sum)
#N5
print("Вывод N 5")
n = int(input("Введите число "))
fact = 1
for i in range(1,n):
    fact*=i
print(fact)
#N6
print("Вывод N 6")
n = int(input("Введите число "))
for i in range(1, 11):
    print(f"{i} * {n} = ",i * n)
#N7
print("Вывод N 7")
n = input("Введите значения ")
a = n.split()
sum = 0
for i in a:
    if int(i) %2 == 0:
        sum+=1
print(sum)
#N8
print("Вывод N 8")
a = input()
sum=0
glas = ['у','е','а','о','э','я','и','ю','ы','ё']
for i in a:
    if i.lower() in glas:
        sum+=1
print(sum)

#N9
print("Вывод N 9")
a = input("Введите список чисел ").split()
b = a[0]
for i in a:
    if i > b:
        b=i
print(b)
# N10
print("Вывод N 10")
for i in range(1,10):
    for j in range(1,10):
        print(f"{i * j:2}", end=" ")
    print()


#while
#N1
print("Вывод N 1")
i=1
while(i <= 10):
    print(i)
    i+=1
#N2
print("Вывод N 2")
i = int(input("Введите число "))
sum = 0
while(i):
    sum+=i
    i=int(input("Введите число "))
print(f"сумма: {sum}")
#N3
print("Вывод N 3")
i = int(input("Введите число "))
sum=0
while(i):
    i//=10
    sum+=1
print(f"количество чисел: {sum}")

#N4
print("Вывод N 4")
i = int(input("Введите число "))
sum=0
while(i):
    b= i%10
    sum+=b
    i//=10
print(f"сумма цифр: {sum}")
#N5
print("Вывод N 5")
i=int(input("Введите число "))
s=""
while(i):
    s += str(i%10)
    i//=10
print(f"обратный порядок: {s}")

#N6
print("Вывод N 6")
i = int(input("Введите число "))
n=2
if i < n:
    print("нет степени 2 выше")
else:
    while(i >= n):
        print(n)
        n*=2

#N7
print("Вывод N 7")
true_pass = "12345"
password = input("Введите пароль ")
while (password != true_pass):
    print("Неверный пароль")
    password = input("Введите пароль ")
print("Вы ввели правильный пароль")
#N8
print("Вывод N 8")
a = int(input("Введите число "))
b = int(input("Введите число "))
while(b!=0):
    a,b = b, a%b
print(f"Наибольший общий делитель: {a}")
#N9
print("Вывод N 9")
n = int(input("Введите число "))
i=1
b=0
if i > n:
    print("число слишком маленькое")
else:
    while(n >= b):
        print(b, end=" ")
        i,b = b, i + b
print()
#N10
print("Вывод N 10")
a = random.randint(1, 100)
b = int(input("введите число: "))
sum=0
while (a != b):
    sum+=1
    if a > b:
        print("Число больше")
    else:
        print("число меньше")
    b = int(input("введите число: "))
print(f"Вы угадали число {a} за {sum} попыток")