monthly_inc = float(input("Enter your monthly income: "))
monthly_exp = float(input("Enter you total monthly expenses: "))
monthly_savings = monthly_inc - monthly_exp

proj_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Your monthly savings are ${int(monthly_savings)}.")
print(f"Projected savings after one year, with interest, is: ${int(proj_savings)}.")
