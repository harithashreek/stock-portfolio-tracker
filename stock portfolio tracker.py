# Stock Portfolio Tracker

# Dictionary containing stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 145
}

total_investment = 0

# Number of stocks the user wants to enter
n = int(input("Enter the number of stocks: "))

for i in range(n):
    stock = input("Enter stock name (AAPL/TSLA/GOOGL/MSFT/AMZN): ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        investment = stock_prices[stock] * quantity
        total_investment += investment
    else:
        print("Stock not found!")

print("\nTotal Investment Value = $", total_investment)

# Save the result in a text file
with open("portfolio.txt", "w") as file:
    file.write("Total Investment Value = $" + str(total_investment))

print("Result saved in portfolio.txt")
