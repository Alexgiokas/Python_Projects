#Ergaisia 1
# Program to calculate total weight and average weight
# of 25 packages

#total weight of the packages
totalWeight = 0

# iterate over the 25 packages
for i in range(25):
    weight = float(input("Βαλε το βαρος του δεματος " +  str(i+1) + ": "))
    totalWeight = totalWeight + weight

# calculate average weight
averageWeight = totalWeight/25

# display total and average weight
print("Συνολικο βαρος:", totalWeight, "κιλα")
print("Μεσος ορος:", averageWeight, "κιλα")




