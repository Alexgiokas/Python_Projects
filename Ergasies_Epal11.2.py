promoted_count = 0
rejected_count = 0

for i in range(1, 5):
    grade = float(input(f"Enter the general grade of student {i}: "))
    if grade >= 9.5:
        print("Promoted")
        promoted_count += 1
    else:
        print("Rejected")
        rejected_count += 1

print(f"Number of promoted students: {promoted_count}")
print(f"Number of rejected students: {rejected_count}")
