"""
Personal Finance Calculator
Student: [Nontana Phubun]
Date: [28 july]
Purpose: Calculate monthly budget and savings
"""

monthly_income = float(input("Enter your monthly income (THB): "))
rent_cost = float(input("Enter your rent or housing cost (THB): "))
food_budget = int(input("Enter your monthly food budget (THB): "))
transportation_cost = float(input("Enter your monthly transportation cost (THB): "))
entertainment_budget = int(input("Enter your entertainment budget (THB): "))
emergency_fund_percent = float(input("Enter percentage for emergency fund (e.g., 10.0): "))
investment_percent = float(input("Enter percentage for investment (e.g., 15.0): "))

total_fixed_expenses = rent_cost + transportation_cost

total_variable_expenses = food_budget + entertainment_budget

total_expenses = total_fixed_expenses + total_variable_expenses

remaining_income = monthly_income - total_expenses

emergency_fund_amount = monthly_income * (emergency_fund_percent / 100)

investment_amount = monthly_income * (investment_percent / 100)

available_for_savings = remaining_income - emergency_fund_amount - investment_amount

expense_ratio = (total_expenses / monthly_income) * 100

print("\n=== MONTHLY BUDGET REPORT ===")
print(f"Income: {monthly_income:.2f} THB")
print(f"Fixed Expenses: {total_fixed_expenses:.2f} THB")
print(f"Variable Expenses: {total_variable_expenses:.2f} THB")
print(f"Total Expenses: {total_expenses:.2f} THB")
print(f"Remaining: {remaining_income:.2f} THB")

print("\n=== SAVINGS BREAKDOWN ===")
print(f"Emergency Fund ({emergency_fund_percent}%): {emergency_fund_amount:.2f} THB")
print(f"Investment ({investment_percent}%): {investment_amount:.2f} THB")
print(f"Available for Savings: {available_for_savings:.2f} THB")

print("\n=== ANALYSIS ===")
print(f"Expense Ratio: {expense_ratio:.2f}%")