#Ergasia_4
weights = []

# Loop to get the weights of 16 students from the user
for i in range(16):
    weight = float(input("Enter weight in kilograms of student #" + str(i+1) + ": "))
    weights.append(weight)

# Calculate the average
average_weight = sum(weights) / len(weights)

# Print the result
print("The average weight of the 16 students is:", average_weight)