#--------------program to compare two numbers & print whether the first is greater,smaller, or equal to the second using relational oprator----------------

# Input: Two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the two numbers
if num1 > num2:
    print(f"The first number {num1} is greater than the second number ({num2}).")
elif num1 < num2:
    print(f"The first number {num1} is smaller than the second number ({num2}).")
else:
    print(f"The first number {num1} is equal to the second number ({num2}).")