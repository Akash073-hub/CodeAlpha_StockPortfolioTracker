stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}
portfolio = {}
total_value = 0
print(" Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))
while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock in stock_prices:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = quantity
    else:
        print(" Invalid stock symbol. Try again.")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    print(f"{stock}: ₹{price} × {qty} = ₹{value}")
print(f"\n Total Investment: ₹{total_value}")

# Optional: File handling
save = input("Do you want to save this to a file? (yes/no): ").lower()
if save == 'yes':
    with open("portfolio_summary.txt", "w") as f:
        f.write("Stock Portfolio Summary:\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            f.write(f"{stock}: ₹{price} × {qty} = ₹{value}\n")
        f.write(f"\nTotal Investment: ₹{total_value}")
    print("Summary saved to 'portfolio_summary.txt'")
