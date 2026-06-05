# List of stock quantities
stock = [25, 5, 0, 12, 3, 18, 0, 30]

out_of_stock = []
restock_required = []
healthy_stock = []
available_products = 0

for qty in stock:
    if qty == 0:
        out_of_stock.append(qty)

    if qty < 10:
        restock_required.append(qty)

    if qty > 0:
        available_products += 1

    if qty >= 15:
        healthy_stock.append(qty)

print("Out of Stock Products:", len(out_of_stock))
print("Restock Required:", restock_required)
print("Available Products:", available_products)
print("Healthy Stock:", healthy_stock)