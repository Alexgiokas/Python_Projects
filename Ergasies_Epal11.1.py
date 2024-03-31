high_salary_count = 0
for i in range(5):
    salary = float(input(f"Enter the salary of employee {i+1}: "))
    if salary > 1500:
        print("High salary")
        high_salary_count += 1
    else:
        print("Low salary")

print("Number of high salary employees:", high_salary_count)