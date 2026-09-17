
a = int(input("Сколько чисел будет в примере "))
numbers = []
opperands = []
for i in range(a):
    numbers.append(float(input("Введите число: ")))
    print(numbers)
c = a - 1
for i in range(c):
    opperands.append(input("Введите знак: "))
result = numbers[0]

for i in range(len(opperands)):
    if opperands[i] == "+" or opperands[i] == "Плюс":
        result += numbers[i + 1]
    elif opperands[i] == "-" or opperands[i] == "Минус":
        result -= numbers[i + 1]
    elif opperands[i] == "*":
        result *= numbers[i + 1]
    elif opperands[i] == "//":
        if int(numbers[i + 1]) is 0:
            print("На ноль делить нельзя")
            result = None
        else:
            result //= numbers[i + 1]
    elif opperands[i] == "/":
        if numbers[i + 1] != 0:
            result /= numbers[i + 1]
        else:
            print("На ноль делить нельзя")
            result = None
    elif opperands[i] == "%":
        result %= numbers[i + 1]
    elif opperands[i] == "**":
        result **= numbers[i + 1]
    else:
        print("Неверный знак")

print(result)
