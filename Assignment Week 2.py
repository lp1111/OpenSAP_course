"""
In this exercise you are going to simulate a sales and operations planning using the zero stock level strategy.
Write a Python program that asks the user to enter the following data:

An initial stock level for a product
The number of month(s) to plan
The planned sales quantity for each month
Based on this data, calculate the required production quantity as follows:

If the sales quantity is smaller than the stock level of the previous month, the production quantity is 0
If the sales quantity is larger than the stock level of the previous month, the production quantity is this difference
"""

initial_stock = int(input("Enter initial stock level:",))
month_plan = int(input("Enter the number of month(s) to plan:",))
production = 0

planned_sales_qty = []

for month in list(range(month_plan)):
    sales_qty = int(input("Enter the planned sales quantity for month" + " " + str(month + 1) + ": "))
    planned_sales_qty.append(sales_qty)

print("The resulting production quantities are:")
for i in list(range(len(planned_sales_qty))):
    if planned_sales_qty[i] > initial_stock:
        production = planned_sales_qty[i] - initial_stock
        print("Production quantity month" + " " + str(i + 1) + " " + "-" + " " + str(production))
        initial_stock = initial_stock + production - planned_sales_qty[i]
    else:
        print("Production quantity month" + " " + str(i + 1) + " " + "-" + " 0")
        initial_stock = initial_stock - planned_sales_qty[i]

