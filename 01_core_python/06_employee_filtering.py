employees = [{'Name': "Carlos", "salary":  2700, "department": "IT"},
            {'Name': "Ana", "salary": 1800, "department": "Sales"},
            {'Name': "John", "salary": 1400, "department": "IT"},
            {'Name': "Ron", "salary": 1300, "department": "Sales"},
            {'Name': "Maria", "salary": 2200, "department": "Sales"}
            
            ]
# for employee in employees:
#     if employee["department"] == "IT" and employee["salary"] > 1500:
#         print(employee["Name"], "IT high salary")
    
#     elif employee["department"] == "Sales" and employee["salary"] > 1500:
#         print(employee["Name"], "Sales high salary")
        
#     else:
#         print(employee["Name"], "does not qualify")
for employee in employees:
    if employee["department"] == "IT" or employee["salary"] >= 1500:
        print(employee["Name"])