#Ergasia_2
# Initialize variables
total_height = 0


# Read in height of 20 students
for i in range(5):
    student_height = int(input("Enter height of student " + str(i+1) + ": "))
    total_height += student_height

# Calculate average height of students
average_height = total_height / 5

# Print average height of students
print("The average height of the students is: " + str(average_height) + " cm.")