
num1 = float(input("Enter the first number:"))
opn = input("Enter the operator:")
num2 = float(input("Enter the second number:"))

if opn == "+":
    print(num1 + num2)
elif opn == "-":
    print(num1 - num2)
elif opn == '*':
    print(num1 * num2)
elif opn == "/":
    print(num1 / num2)
else:
    print("\n Invalid operation")

