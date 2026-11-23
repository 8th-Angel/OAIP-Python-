
# 1
print("Вывод 1:")
def say_hi():
    print("Привет!")

other = say_hi
other()


# 2
print("Вывод 2:")
def cube(x):
    return x ** 3

first_name = cube
second_name = cube

print(first_name(2))
print(second_name(3))


# 3
print("Вывод 3:")
def get_five():
    return 5

print(type(get_five))
print(type(get_five()))


# 4
print("Вывод 4:")
def greet():
    print("Добро пожаловать!")

def run(action):
    action()

run(greet)


# 5
print("Вывод 5:")
def double(x):
    return x * 2

def apply(action, number):
    return action(number)

print(apply(double, 6))


# 6
print("Вывод 6:")
def add_ten(x):
    return x + 10

def transform(values, action):
    return [action(v) for v in values]

print(transform([1, 2, 3], add_ten))


# 7
print("Вывод 7:")
def factory():
    def inner():
        print("Работает")
    return inner

worker = factory()
worker()


# 8
print("Вывод 8:")
def make_adder(value):
    def adder(number):
        return number + value
    return adder

add_five = make_adder(5)
print(add_five(7))


# 9
print("Вывод 9:")
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

c = make_counter()
print(c())
print(c())
print(c())