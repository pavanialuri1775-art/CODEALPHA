# Stock Portfolio Tracker

A Python project that calculates stock investment values using predefined stock prices and stores the results in a text file.

## Features
- User can enter stock names and quantities
- Calculates investment value for each stock
- Calculates total investment value
- Stores portfolio details in a text file
- Uses dictionary data structure

## Code

```python
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
```

## Concepts Used
- Dictionaries
- Loops
- Conditional Statements
- File Handling
- User Input Handling
- Arithmetic Operations

## Output File
The program creates a file named `portfolio.txt` to store investment details.

## Author
Pavani
