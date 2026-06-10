# roblem Statement 
# Delivery times (in minutes) for different orders are given below: 
# delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18] 
# Requirements 
# Create the following functions: 
# 1. fastest_delivery(times) 
# Returns the shortest delivery time. 
# 2. delayed_orders(times) 
# Returns a list of orders taking more than 45 minutes. 
# 3. average_delivery_time(times) 
# Returns the average delivery time. 
# 4. delivery_category(times) 
# Displays order categories: 
# • Fast → ≤ 30 minutes  
# • Normal → 31–45 minutes  
# • Delayed → > 45 minutes 

delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

#fastest_delivery
def fastest_delivery(times):
    #find the shortest delivery time
    shortest = min(times)
    #return the shortest delivery time
    return shortest

#delayed_orders
def delayed_orders(times):
    #create a list of orders taking more than 45 minutes
    delayed = []
    for time in times:
        if time > 45:
            delayed.append(time)
    #return the list of orders taking more than 45 minutes
    return delayed

#average_delivery_time
def average_delivery_time(times):
    #calculate the average delivery time
    total = sum(times)
    average = total / len(times)
    #return the average delivery time
    return average

#delivery_category
def delivery_category(times):
    #create a list of order categories
    categories = {}
    for time in times:
        if time <= 30:
            if time not in categories:
                categories[time] = "Fast"

        elif time <= 45:
            if time not in categories:
                categories[time] = "Normal"
        
        else:
            if time not in categories:
                categories[time] = "Delayed"
    
    #return the list of order categories
    return categories


print("fastest_delivery:",fastest_delivery(delivery_time),"minutes")
print("delayed_orders:",delayed_orders(delivery_time))
print("average_delivery_time:",average_delivery_time(delivery_time),"minutes")
print("delivery_category:",delivery_category(delivery_time))

'''
Output:
fastest_delivery: 18 minutes
delayed_orders: [60,80,55]
average_delivery_time: 40.8 minutes
delivery_category: {28: 'Fast', 45: 'Normal', 60: 'Delayed', 22: 'Fast', 35: 'Normal', 80: 'Delayed', 40: 'Normal', 25: 'Fast', 55: 'Delayed', 18: 'Delayed'}

'''