# ⌨️ Get gross income and expenses from the user
# ℹ️ input() reads values as text (strings), so float() converts them to numbers with decimals for calculation

gross_income = float(input("What is your gross monthly income?  "))
housing = float(input("What do you spend on your rent or mortgage?  "))
phone = float(input("What do you spend on your phone each month?  "))


# ✂️ Calculate net income assuming a 20% tax deduction (retaining 80%)
net_income = gross_income * 0.8

# ➕ Sum up monthly costs
total_expenses = phone + housing

# 💵 Find the remaining disposable income
remaining = net_income - total_expenses

# 📊 Format and display total expenses
# 💰 `$` prints as a literal dollar sign in front
# 🎯 `,` adds thousand separator commas
# 🎯 `.2f` specifies 2 decimal places of floating-point precision
print(f"You spent a  total of ${total_expenses:,.2f}")

# 📈 Calculate and display the expenses as a percentage of net income
# 🎯 `total_expenses/net_income` does inline division
# 🎯 `.2%` multiplies the result by 100, rounds to 2 decimal places, and appends the % sign
print(f"That was {total_expenses/net_income:.2%} of your net income")
