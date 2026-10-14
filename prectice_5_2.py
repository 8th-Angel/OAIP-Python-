#N1
print("Вывод N1")
a = {
    "Паша":5,
    "Маша":5,
    "Саша":4
    }
print(a["Паша"],a["Маша"],a["Саша"])
#N2
print("Вывод N2")
a = {
    "Паша":5,
    "Маша":5,
    "Саша":4
    }
a["Даша"] = 3
a["Саша"] = 5
del a["Маша"]
print(a)
#N3
print("Вывод N3")
a = {
    "Паша":5,
    "Маша":5,
    "Саша":4
    }
key = "Даша"
if key in a:
    print(a[key])
else:
    print("Нет такого ключа.")
#N4
print("Вывод N4")
a = {
    "Паша":5,
    "Маша":5,
    "Саша":4
    }
print(list(a.keys()))
print(list(a.values()))
print(len(a))
#N5
print("Вывод N5")
a = {
    "Планшет":50000,
    "ноутбук":100000,
    "телефон":40000
    }
print(*a.items(), sep="\n")
#N6
print("Вывод N6")
a = {
    "Планшет":50000,
    "ноутбук":100000,
    "телефон":40000
    }
sum1 = sum(a.values())
max1 = max(a, key=a.get)
print(f"сумма: {sum1}, самый дорогой товар: {max1}")
#N7
print("Вывод N7")
text = "телефон"
a={}
for char in text:
    a[char] = a.get(char, 0) + 1
print(a)
#N8
print("Вывод N8")
a = "банан яблоко яблоко"
b = a.split()
d = {}
for word in b:
    d[word] = d.get(word, 0) + 1
answer = max(d, key = d.get)
print(f"Самое частое слово: {answer}")
#N9
print("Вывод N9")
a = {
    "Планшет":50000,
    "ноутбук":100000,
    "телефон":40000
    }
b = {}
for key, value in a.items():
    b[value] = key
print(b)
#N10
print("Вывод N10")
a = ["Россия","Франция","Великобритания"]
b = ["Москва","Париж","Лондон"]
user = input("Введите страну ")
c = dict(zip(a,b))
print(c.get(user))