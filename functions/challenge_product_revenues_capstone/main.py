# 1. Daten
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]
quantities_sold = [150, 200, 100, 50]

# 2. Berechnung der Umsätze
def calculate_revenue(prices, quantities_sold):
    revenue = []
    for p, q in zip(prices, quantities_sold):
        revenue.append(p * q)
    return revenue

# 3. Ausgabe im geforderten Format
def formatted_output(revenues):
    # revenues ist hier der Parameter, nicht `revenue`
    revenue_per_product = sorted(zip(products, revenues))
    for name, rev in revenue_per_product:
        print(f"{name} has total revenue of ${rev}")

# 4. Aufrufe in der richtigen Reihenfolge
revenue = calculate_revenue(prices, quantities_sold)
revenue_per_product = list(zip(products, revenue)) 
formatted_output(revenue)