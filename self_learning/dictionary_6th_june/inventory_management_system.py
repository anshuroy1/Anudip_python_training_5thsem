#  Display products with stock less than 10.
#  Count products having stock more than 50.
# Find the product with the minimum stock.
#  Create a list of products that require restocking (stock < 20).
#  Calculate the total inventory count.


# Program: Inventory Management System


# Dictionary containing product names and stock quantity
inventory = {
    "Notebook": 45,
    "Pen": 120,
    "Pencil": 80,
    "Eraser": 25,
    "Marker": 15,
    "Stapler": 8,
    "Glue": 12,
    "Scale": 30,
    "Folder": 5,
    "Calculator": 3
}


# 1. Display products with stock less than 10


print("Products with stock less than 10:")

for product, stock in inventory.items():

    if stock < 10:
        print(product, ":", stock)


# 2. Count products having stock more than 50


count = 0

for stock in inventory.values():

    if stock > 50:
        count += 1

print("\nProducts having stock more than 50:", count)


# 3. Find product with minimum stock


min_product = ""
min_stock = float('inf')

for product, stock in inventory.items():

    if stock < min_stock:
        min_stock = stock
        min_product = product

print("\nProduct with Minimum Stock:")
print(min_product, ":", min_stock)


# 4. Create list of products requiring restocking
#    (stock less than 20)


restock_list = []

for product, stock in inventory.items():

    if stock < 20:
        restock_list.append(product)

print("\nProducts Requiring Restocking:")
print(restock_list)


# 5. Calculate total inventory count


total_stock = 0

for stock in inventory.values():
    total_stock += stock

print("\nTotal Inventory Count:", total_stock)