def check_scholarship(age, annual_income):
    if age < 25 and annual_income < 300000:
        return "Eligible for the specialized education scholarship."
    else:
        return "Not eligible for the specialized education scholarship."



age = int(input("Enter applicant's age: "))
annual_income = float(input("Enter annual family income: "))


result = check_scholarship(age, annual_income)
print(result)