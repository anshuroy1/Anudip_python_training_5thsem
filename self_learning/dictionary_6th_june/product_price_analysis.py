# • Display products costing more than ₹5000.
# •Count products costing less than ₹3000.
# • Find the most expensive product.
# • Create a list of products priced between ₹2000 and ₹10000.
# • Calculate the total value of all products.

# Product Price Analysis

prices = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1800,
    "Monitor": 12000,
    "Printer": 9000,
    "Tablet": 28000,
    "Speaker": 3500,
    "Webcam": 2500,
    "Headphones": 4200,
    "Router": 3200
}

# 1. Display products costing more than 5000


print("Products Costing More Than 5000:")

for product, price in prices.items():

    if price > 5000:
        print(product, ":", price)


# 2. Count products costing less than 3000


count = 0

for price in prices.values():

    if price < 3000:
        count += 1

print("\nProducts Costing Less Than 3000:", count)


# 3. Find the most expensive product


highest_product = ""
highest_price = 0

for product, price in prices.items():

    if price > highest_price:
        highest_price = price
        highest_product = product

print("\nMost Expensive Product:")
print(highest_product, ":", highest_price)

# 4. Create a list of products priced between
#    2000 and 10000


product_list = []

for product, price in prices.items():

    if price >= 2000 and price <= 10000:
        product_list.append(product)

print("\nProducts Priced Between 2000 and 10000:")
print(product_list)


# 5. Calculate total value of all products


total_value = 0

for price in prices.values():
    total_value += price

print("\nTotal Value of All Products:", total_value)