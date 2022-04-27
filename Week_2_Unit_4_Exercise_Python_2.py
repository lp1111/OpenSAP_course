"""Instructions:
Now it's your turn. Click the button below to open CodeOcean and implement a solution for the given exercise. If you want, you can also solve it in a
Jupyter Notebook first and copy the solution to CodeOcean afterwards.
Your are given the following list containing stock symbols, their current price as well as the absolute price change of the previous day:
As you plan to take some of the profits, write a program that creates a list of all the stock symbols with a change of more than +5 percent. The list should
be named sell_list. The list should only contain the stock symbol, not the price or the absolute change. Print the resulting list.
"""
stocks = [["SAP", 106, -3.0], ["AAPL", 165, 1.25], ["TSLA", 860, 54.2], ["ORCL", 76, -0.25], ["ZM", 114, 6.2]]

sell_list = []



for i in range(len(stocks)):
    if stocks[i][2] / (stocks[i][1] + stocks[i][2]) > .05:
        sell_list.append(stocks[i][0])

print(sell_list)
