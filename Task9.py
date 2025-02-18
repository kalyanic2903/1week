# ------------program that takes two integers and performs both floor division(//) and modulo(%) operations-----------

# Input: Two integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Floor division and Modulo operations
floor_division = num1 // num2
modulo = num1 % num2

# Print results
print(f"The result of floor division ({num1} // {num2}) is: {floor_division}")
print(f"The result of modulo ({num1} % {num2}) is: {modulo}")