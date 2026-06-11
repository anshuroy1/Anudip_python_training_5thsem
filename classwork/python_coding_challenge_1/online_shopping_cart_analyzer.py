# roblem 5: Online Shopping Cart Analyzer 
# Problem Statement 
# The prices of products added to a shopping cart are stored below. 
# Sample Data 
# cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999] 
# Tasks 
# 1. Calculate the total cart value.  
# 2. Find the most expensive and cheapest products.  
# 3. Count products eligible for premium shipping (price > ₹1000).  
# 4. Generate a discount list (products above ₹1500).  
# 5. Calculate the average product price.

cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999]

#1. Calculate the total cart value
total_value = sum(cart)
print("Total cart value:", total_value)

#2. Find the most expensive and cheapest products
max_price = max(cart)
min_price = min(cart)
print("Most expensive product:", max_price)
print("Cheapest product:", min_price)

#3. Count products eligible for premium shipping
premium = 0 
for price in cart:
    if price > 1000:
        premium += 1
print("Number of products eligible for premium shipping:", premium)

#4. Generate a discount list (products above ₹1500)
discount_list = []
for price in cart:
    if price > 1500:
        discount_list.append(price)
print("Discount list:", discount_list)

#5. Calculate the average product price
average_price = sum(cart) / len(cart)
print("Average product price:", average_price)