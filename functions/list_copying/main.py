# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

def apply_discount(prices):
    # Copy the function’s input list
    prices_copy = prices.copy()
    # Iterate by index over the copied list
    for i in range(len(prices_copy)):
        # Check the price value, not the index
        if prices_copy[i] > 2.00:
            prices_copy[i] *= 0.90  # apply 10% discount
    return prices_copy

# Call the function correctly with the original list
updated_prices = apply_discount(product_prices)
print(f"Updated product prices: {updated_prices}")