list_of_keys = ["name", "email"]

employee = {
    "name": "John",
    "email": "john@ecorp.com",
    "access_level": 5,
    "age": 28
}

for key in list_of_keys:
    employee.pop(key, None)

print(employee)