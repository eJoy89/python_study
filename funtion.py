def add(a, b):
    return a + b

print(add(7, 5))

a = add(3, 4)
print(a)

def say():
    return 'hi'

a = say()
print(a)

def sub(a, b):
    return a - b
print(sub(10, 3))

def add(a, b):
    return a + b

result = add(a = 3, b = 5)

print(result)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul('add', 1,2,3,4,5)
print(result)
result1 = add_mul('mul', 1,2,3,4,5)
print(result1)