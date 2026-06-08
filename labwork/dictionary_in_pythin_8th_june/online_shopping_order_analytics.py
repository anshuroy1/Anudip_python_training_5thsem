# Problem Statement 
# An e-commerce company stores product sales data as: 
# sales = { 
#     "Laptop": 15, 
#     "Mouse": 45, 
#     "Keyboard": 32, 
#     "Monitor": 12, 
#     "Headphones": 28, 
#     "Printer": 8, 
#     "Webcam": 20, 
#     "Speaker": 18, 
#     "Tablet": 10, 
#     "Router": 25 
# } 
# Tasks 
# 1. Display products sold more than 20 times.  
# 2. Find the best-selling product.  
# 3. Find the least-selling product.  
# 4. Calculate total products sold.  
# 5. Create a list of products requiring promotion (sales < 15).  
# 6. Count products having sales between 10 and 30.  

# creating a dictionary to store product sales data
sales = { 
    "Laptop": 15, 
    "Mouse": 45, 
    "Keyboard": 32, 
    "Monitor": 12, 
    "Headphones": 28, 
    "Printer": 8, 
    "Webcam": 20, 
    "Speaker": 18, 
    "Tablet": 10, 
    "Router": 25 
}
#--------------------------------------------------
# to display products sold more than 20 times   
print("Products sold more than 20 times : ")
for product, quantity in sales.items():
    if quantity > 20:
        print(product)  
#--------------------------------------------------
# to find the best-selling product
best_product = ""
highest_sale = 0
for product, sale in sales.items():
    if sale > highest_sale:
        highest_sale = sale
        best_product = product
print("Best-selling product : ", best_product)
#--------------------------------------------------

# to find the least-selling product
products = list(sales.keys())
least_product = products[0]
lowest_sale = sales[least_product]
for product in products:
    if sales[product] < lowest_sale:
        lowest_sale = sales[product]        
        least_product = product
print("Least-selling product : ", least_product)

#-------------------------------------------------- 
# to calculate total products sold
total_sales = 0 
for sale in sales.values():
    total_sales += sale

print("Total products sold : ", total_sales)
#--------------------------------------------------

# to create a list of products requiring promotion (sales < 15)
promotion_products = []
for product, sale in sales.items():
    if sale < 15:
        promotion_products.append(product)
print("Products requiring promotion : ", promotion_products)
#-------------------------------------------------- 
# to count products having sales between 10 and 30
count = 0
for sale in sales.values():
    if 10 <= sale <= 30:
        count += 1

print("Number of products having sales between 10 and 30 : ", count)    

'''
output:

Products sold more than 20 times : 
Mouse       
Keyboard
Headphones
Router

Best-selling product :  Mouse
Least-selling product :  Printer
Total products sold :  213

Products requiring promotion :  ['Laptop', 'Monitor', 'Printer', 'Tablet']
Number of products having sales between 10 and 30 :  6

'''