#Simple calculations
num1 = int(input("Enter the first num"))
num2 = int(input("Ente the second num"))
operator = input("Enter the operator(+,-,*,/)")

if operator =="+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    result = "Invalid operator"

print("Result", result)
