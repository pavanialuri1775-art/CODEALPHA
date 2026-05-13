#
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 300
}
total_investment = 0
file = open("portfolio.txt", "w")
while True:
    stock_name = input("Enter stock name: ").upper()
    if stock_name == "EXIT":
        break
    if stock_name in stocks:
        quantity = int(input("Enter quantity: "))
        investment = stocks[stock_name] * quantity
        total_investment += investment
        print("Investment value:", investment)
        file.write(f"{stock_name} - {quantity} shares = {investment}\n")
    else:
        print("Stock not found")
print("\nTotal Investment Value:", total_investment)
file.write(f"\nTotal Investment Value: {total_investment}")
file.close()