# Problem Statement
# An online store wants to manage products and sales.
# Example Structure
# products = {
# "P101": {
# "name": "Laptop",
# "price": 55000,
# "stock": 12,
# "sold": 25
# }
# }
# Maintain records of at least 30 products.
# Requirements
# 1. Display all products.
# 2. Add a new product.
# 3. Update stock after sales.
# 4. Find out-of-stock products.
# 5. Find products with stock less than 5.
# 6. Calculate total inventory value.
# 7. Find best-selling product.
# 8. Find least-selling product.
# 9. Calculate total revenue generated.
# 10. Generate a low-stock report.
# 11. Display products whose sales exceed the average sales.
# 12. Create a dictionary of products eligible for promotion (sales < 10).
# Challenge
# Generate a complete business report.


#empty dictionary to store product records
products = {}

while True:
    product_id = input("Enter product ID : ")

    #validate product id
    if product_id in products:
        print("Product ID already exists. Please enter a unique ID.")
        continue

    elif not product_id.isalnum():
        print("Invalid product ID. Please enter a valid ID.")
        continue

    name =input("Enter product name : ")

    #validate product name
    if not name.isalpha():
        print("Invalid product name. Please enter a valid name.")
        continue

    price = int(input("Enter product price : "))

    #validate product price
    if price < 0:
        print("Invalid product price. Please enter a valid price.")
        continue

    stock = int(input("Enter product stock : "))

    #validate product stock
    if stock < 0:
        print("Invalid product stock. Please enter a valid stock.")
        continue

    sold = int(input("Enter product sold : "))

    #validate product sold
    if sold < 0:
        print("Invalid product sold. Please enter a valid sold.")
        continue

    
    products[product_id] = {
        "name": name,
        "price": price,
        "stock": stock,
        "sold": sold
    }

    choice = input("Do you want to add more products? (yes/no) : ")
    if choice.lower() != "yes":
        break


#1. Display all products.
print("All products:")
for product_id, details in products.items():
    print(f"Product ID: {product_id}")
    print(f"Name: {details['name']}")
    print(f"Price: {details['price']}")
    print(f"Stock: {details['stock']}")
    print(f"Sold: {details['sold']}")
    print()


#2. Add a new product.
product_id = input("Enter product ID : ")

#validate product id
if product_id in products:
    print("Product ID already exists. Please enter a unique ID.")
    exit()

elif not product_id.isalnum():
    print("Invalid product ID. Please enter a valid ID.")
    exit()

else:

  name =input("Enter product name : ")

  #validate product name
  if not name.isalpha():
    print("Invalid product name. Please enter a valid name.")
    exit()

  price = int(input("Enter product price : "))

  #validate product price
  if price < 0:
    print("Invalid product price. Please enter a valid price.")
    exit()

  stock = int(input("Enter product stock : "))

  #validate product stock
  if stock < 0:
    print("Invalid product stock. Please enter a valid stock.")
    exit()

  sold = int(input("Enter product sold : "))

  #validate product sold
  if sold < 0:
    print("Invalid product sold. Please enter a valid sold.")
    exit()

  #add new product
  products[product_id] = {
    "name": name,
    "price": price,
    "stock": stock,
    "sold": sold
}

print("Product added successfully.")


#3. Update stock after sales.
product_id = input("Enter product ID : ")

if product_id in products:

    sold = int(input("Enter sold quantity : "))

    #validate product sold
    if sold < 0:
        print("Invalid product sold. Please enter a valid sold.")
        exit()

    #update sold quantity   
    products[product_id]["sold"] += sold

    #update stock

    #check if stock is enough
    if products[product_id]["stock"] < sold:
        print("Insufficient stock.")
        exit()
    else:
       
       #update stock
       products[product_id]["stock"] -= sold
       print("Stock updated successfully.")
else:
    print("Product not found.")


#4. Find out-of-stock products.
print("Out-of-stock products:")
for product_id, details in products.items():
    if details["stock"] == 0:
        print(f"Product ID: {product_id}")
        print(f"Name: {details['name']}")
        print()


#5. Find products with low stock.
print("Products with low stock:")
for product_id, details in products.items():
    if details["stock"] < 5:
        print(f"Product ID: {product_id}")
        print(f"Name: {details['name']}")
        print(f"Stock: {details['stock']}")
        print()


#6. Calculate total inventory value.
total_value = 0
for product_id, details in products.items():
    total_value += details["price"] * details["stock"]

print(f"Total inventory value: {total_value}")


#7. find best-selling product.
best_selling_product = (list(products.keys()))[0]
for product_id, details in products.items():
    if details["sold"] > products[best_selling_product]["sold"]:
        best_selling_product = product_id
        best_selling_product_quantity = details["sold"]

print(f"Best-selling product: {best_selling_product} with {best_selling_product_quantity} sales")


#8. find least-selling product.

#get least of product id
least_selling_product = (list(products.keys()))[0]


for product_id, details in products.items():
    if details["sold"] < products[least_selling_product]["sold"]:
        least_selling_product = product_id
        least_selling_product_quantity = details["sold"]

print(f"Least-selling product: {least_selling_product} with {least_selling_product_quantity} sales")


#9. calculate total revenue generated.
total_revenue = 0
for product_id, details in products.items():
    total_revenue += details["price"] * details["sold"]

print(f"Total revenue generated: {total_revenue}")


#10. generate a low-stock report.
print("Low-stock report:")
for product_id, details in products.items():
    if details["stock"] < 5:
        print(f"Product ID: {product_id}")
        print(f"Name: {details['name']}")
        print(f"Stock: {details['stock']}")
        print()


#11. Display products whose sales exceed the average sales.

#get average of sales
total_sales = 0
for product_id, details in products.items():
    total_sales += details["sold"]

#calculate average
average_sales = total_sales / len(products)

#display products
print("Products with sales above average:")
for product_id, details in products.items():
    if details["sold"] > average_sales:
        print(f"Product ID: {product_id}")
        print(f"Name: {details['name']}")
        print(f"Sales: {details['sold']}")
        print()


#12. Create a dictionary of products eligible for promotion (sales < 10).
promotion_products={}

for product_id , details in products.items():
    if details["sold"]<10:
        promotion_products[product_id]={
            "name":details["name"],
            "price":details["price"]
            
        }