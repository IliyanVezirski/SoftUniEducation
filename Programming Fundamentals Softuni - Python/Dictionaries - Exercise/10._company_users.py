company_users = {}

company = input()

while company != "End":
    company = company.split(' -> ')
    employee_id = company[1]
    name = company[0]
    if name not in company_users:
        company_users[name] = [employee_id]
    else:
        id = company_users[name]
        if employee_id not in id:
            id.append(employee_id)
            company_users[name] = id
        else:
            company_users[name] = id

    company = input()

for k, v in company_users.items():
    print(f"{k}")
    for value in v:
        print(f"-- {value}")
