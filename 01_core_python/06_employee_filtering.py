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
# for employee in employees:
#     if employee["department"] == "IT" or employee["salary"] >= 1500:
#         print(employee["Name"])

# active_employees = [{"name": "Carlos", "active": True},
#                     {"name": "Ana", "active": False},
#                     {"name": "John", "active": True},
#                     {"name": "Ron", "active": False},
#                 ]
# for employee in active_employees:
#     if not  employee["active"]:
#         print(employee["name"], "is not active")

# employees = [
#     {"name": "Carlos", "department": "IT", "salary": 2700},
#     {"name": "Ana", "department": "Sales", "salary": 1800},
#     {"name": "John", "department": "IT", "salary": 1400},
#     {"name": "Ron", "department": "Sales", "salary": 1300},
    
# ]
# for employee in employees:
#     if employee["department"] == "IT" and employee["salary"] > 1500:
#         print(employee["name"], "is a high paid in IT employee")


employees = [
    {"name": "Carlos", "department": "IT", "salary": 2700, "active": True},
    {"name": "Ana", "department": "Sales", "salary": 1800, "active": True},
    {"name": "John", "department": "IT", "salary": 1400, "active": False},
    {"name": "Ron", "department": "Sales", "salary": 1300, "active": False},
    {"name": "Maria", "department": "IT", "salary": 2200, "active": True}
]

for employee in employees:
    if employee["active"] and (
        employee["department"] == "IT"
        or employee["salary"] >= 1800
    ):
        print(employee["name"])
        
        