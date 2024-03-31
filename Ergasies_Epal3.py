#Ergasia_3
grades = []

# Loop to get 13 grades from the user
for i in range(13):
    grade = float(input("Enter grade #" + str(i+1) + ": "))
    grades.append(grade)

# Calculate the average
average = sum(grades) / len(grades)

# Print the result
print("The average of the 13 grades is:", average)