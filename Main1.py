# Programmer: Theresa DeJacimo
# Course:  CS151, Dr.   Zelalem Jembre Yalew
# Due Date: 9/18/24
# PA: 0
# Problem Statement: What percentage of my mom's monthly income is spent on groceries?
# Data In: Amount of money spent on groceries and monthly income
# Data Out: Percentage of data spent on groceries
# Credits: In class and high school algebra

grocery_spending_month = float ('Ask how much customer spends per month on groceries')
income_per_month = float ('Ask customer how much they make per month')

#Equation to find percentage of income spent on groceries

percentage_of_income_spent_on_groceries = (grocery_spending_month / income_per_month) * 100

print(percentage_of_income_spent_on_groceries, '%')


