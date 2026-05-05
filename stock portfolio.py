stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 300
}

total = 0

n = int(input("How many stocks? "))

for i in range(n):
    name = input("Enter stock name: ").upper()
    qty = int(input("Enter quantity: "))

    if name in stocks:
        total += stocks[name] * qty
    else:
        print("Stock not found!")

print("💰 Total Investment:", total)

# Save to file
with open("portfolio.txt", "w") as f:
    f.write(f"Total Investment: {total}")

print("Saved to file!")