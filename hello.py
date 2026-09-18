def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b


print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == 1:
    print("Result =", addition(a, b))

elif choice == 2:
    print("Result =", subtraction(a, b))

elif choice == 3:
    print("Result =", multiplication(a, b))

elif choice == 4:
    if b != 0:
        print("Result =", division(a, b))
    else:
        print("Cannot divide by zero")

else:
    print("Invalid choice")