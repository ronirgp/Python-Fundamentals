employees = [{'Name': "Carlos", "salary":  2700, "department": "IT"},
            {'Name': "Ana", "salary": 1800, "department": "Sales"},
            {'Name': "John", "salary": 1400, "department": "IT"},
            {'Name': "Ron", "salary": 1300, "department": "Sales"}
        
            ]
# for employee in employees:
#     if employee['salary'] >= 1800:
#         print(employee["Name"], "qualifies")
        
for employee in employees:
    if employee["department"] == "IT" and employee["salary"] > 1500:
        print(employee["Name"], "qualifies") 
    
    