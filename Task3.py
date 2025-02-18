#--------------A given number is even or odd using ternary oprator--------------

# Take input from the user
num = int(input("Enter a number: "))

# Check if the number is even or odd using the ternary operator
result = "Even" if num % 2 == 0 else "Odd"

# Output the result
print(f"The number is {result}.")