a=float(input("Введите a "))
b=float(input("Введите b "))
operand=str(input("Введите операцию "))
if operand == '+':
    print(a + b)
elif operand == '-':
    print(a - b)
elif operand == '*':
    print(a * b)
elif operand == '/':
    if b != 0:
        print(a / b)
    else:
        print('Нельзя делить на ноль')
elif operand == '//':
    if b != 0:
        print(a // b)
    else:
        print('Нельзя делить на ноль')
elif operand == '%':
    if b != 0:
        print(a % b)
    else:
        print('Нельзя делить на ноль')
elif operand == '**':
    print(a ** b)
elif operand == '==':
    print(a == b)
elif operand == '!=':
    print(a != b)
elif operand == '>':
    print(a > b)
elif operand == '<':
    print(a < b)
elif operand == '>=':
    print(a >= b)
elif operand == '<=':
    print(a <= b)
elif operand == 'and':
    print(bool(a and b))
elif operand == 'or':
    print(bool(a or b))
elif operand == 'not':
    print("a", bool(a))
    print("b", bool(b))
elif operand == 'in':
    a = str(a)
    b = str(b)
    print(bool(a in b))
elif operand == 'not in':
    a = str(a)
    b = str(b)
    print(bool(a not in b))
elif operand == 'is':
    print(a is b)
elif operand == 'is not':
    print(a is not b)
else:
    print("Неверная операция")
