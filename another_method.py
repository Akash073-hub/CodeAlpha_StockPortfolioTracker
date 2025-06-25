stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}
total = 0
print("Stock Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))
for stock in stock_prices:
    qty = int(input(f"Enter quantity for {stock}: "))
    total += qty * stock_prices[stock]
print(f"Total Investment: ₹{total}")
