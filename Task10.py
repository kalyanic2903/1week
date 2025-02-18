# Input: Score from the user
score = float(input("Enter the score (0-100): "))

# Determine the grade based on the score
if score >= 90 and score <= 100:
    grade = "A"
elif score >= 80 and score < 90:
    grade = "B"
elif score >= 70 and score < 80:
    grade = "C"
elif score >= 60 and score < 70:
    grade = "D"
elif score >= 0 and score < 60:
    grade = "F"
else:
    grade = "Invalid score!!! Please enter a score between 0 and 100."

# Print the grade
print(f"The grade for a score of is: {grade}")