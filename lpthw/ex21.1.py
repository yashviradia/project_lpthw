def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"multiplying {a} * {b}")
    return a * b

def divide(a, b):
    print(f"dividing {a} / {b}")
    return a / b

mercedes = add(56, 71)
print("Mercedes = ", mercedes)
audi = subtract(98, 35)
print("Audi = ", audi)
bentley = multiply(44, 35)
print("Bentley = ", bentley)
tesla = divide(144444, 2)
print("Tesla = ", tesla)

print("Jetzt ist dieses eine erste Rätsel.")

geraten = add(mercedes, multiply(audi, divide(tesla, subtract(mercedes, multiply(tesla, bentley)))))
print(f"das ist {geraten}, so viele Wagen!")
