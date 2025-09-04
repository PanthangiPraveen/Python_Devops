salaries = {
    "Amit": 25000,
    "uma": 42000,
    "Rajesh": 54500,
    "Praveen": 78000,
    "Sandeep": 51000,
    "Satya": 12000,
    "Neha": 45000,
    "Raj": 62000,
    "Priya": 30000,
    "Karan": 58000,
    "Divya": 70000
}

# salary bands

low_salary = []
Medium_salary = []
High_salary = []

for name,salary in salaries.items():
    if salary < 30000:
        low_salary.append(name)
    elif salary < 60000:
        Medium_salary.append(name)
    else:
        High_salary.append(name)
        
print("low:", ", ".join(low_salary))
