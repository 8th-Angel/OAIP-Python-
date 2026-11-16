#1
def say_hello():
    print("Hello, world!")
say_hello()
say_hello()
#2
def greet(name):
    print(f"Привет, {name}!")
greet("Анна")
greet("Олег")
#3
def add(a,b):
    return a + b
result = add(3, 5)
print(result)
#4
def greet1(name="Гость"):
    print(f"Привет, {name}!")
greet1("Алексей")
greet1()
#5
def subtract(a, b):
    return a - b
result_pos = subtract(10, 4)
print(result_pos)
result_named = subtract(a=10, b=4)
print(result_named)
result_named_reversed = subtract(b=4, a=10)
print(result_named_reversed)
#6
def introduce(name, city="Москва"):
    return f"Меня зовут {name}, я из {city}."
print(introduce("Анна"))
print(introduce("Анна", "Санкт-Петербург"))
#7
def multiply(*numbers):
    if numbers:
        result = 1
        for num in numbers:
            result *= num
        return result
    else:
        return 1

print(multiply(2, 3, 4))
#8
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
display_info(name="Анна", age=25, city="Москва")
#9
def order(order_name, *additionally, sum=1):
    return f"Заказ: {order_name}, количество: {sum}, дополнительно: {additionally}"
order1 = order("Пицца", "Напиток", "Десерт")
print(order1)
order2 = order("Пицца", "Напиток", "Десерт", sum=2)
print(order2)
#10
def profile(name, age=18, **kwargs):
    result = [f"Имя: {name}", f"Возраст: {age}"]
    for key, value in kwargs.items():
        result.append(f"{key}: {value}")
    return result
user1 = profile("Анна", city="Москва", profession="Программист")
print(user1)
