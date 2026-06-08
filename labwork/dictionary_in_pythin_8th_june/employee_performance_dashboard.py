    # Employee performance scores are stored as: 
    # performance = { 
    #     "EMP101": 92, 
    #     "EMP102": 78, 
    #     "EMP103": 45, 
    #     "EMP104": 88, 
    #     "EMP105": 97, 
    #     "EMP106": 56, 
    #     "EMP107": 81, 
    #     "EMP108": 64, 
    #     "EMP109": 39, 
    #     "EMP110": 73 
    # } 
    # Tasks 
    # 1. Display employees scoring above 80.  
    # 2. Count employees needing improvement (score < 60).  
    # 3. Find the top performer.  
    # 4. Calculate average performance score.  
    # 5. Create separate lists:  
    # o Excellent (≥ 90)  
    # o Good (75–89)  
    # o Average (60–74)  
    # o Poor (< 60)  
# creating a dictionary to store employee performance scores
performance = { 
    "EMP101": 92, 
    "EMP102": 78, 
    "EMP103": 45, 
    "EMP104": 88, 
    "EMP105": 97, 
    "EMP106": 56, 
    "EMP107": 81, 
    "EMP108": 64, 
    "EMP109": 39, 
    "EMP110": 73 
} 
#--------------------------------------------------
# to display employees scoring above 80
print("Employees scoring above 80 : ")  
for emp_id, score in performance.items():
    if score > 80:
        print(emp_id)
#--------------------------------------------------
# to count employees needing improvement (score < 60)
improvement_count = 0
for score in performance.values():
    if score < 60:
        improvement_count += 1
print("Number of employees needing improvement : ", improvement_count)
#--------------------------------------------------
# to find the top performer
top_performer = ""
highest_score = 0
for emp_id, score in performance.items():
    if score > highest_score:
        highest_score = score
        top_performer = emp_id
print("Top performer : ", top_performer)
#--------------------------------------------------
# to calculate average performance score
total_score = 0
for score in performance.values():
    total_score += score
average_score = total_score / len(performance)
print("Average performance score : ", average_score)
#--------------------------------------------------

# to create separate lists based on performance categories
excellent = []
good = []
average = []
poor = []
for emp_id, score in performance.items():
    if score >= 90:
        excellent.append(emp_id)
    elif score >= 75:
        good.append(emp_id)
    elif score >= 60:
        average.append(emp_id)
    else:
        poor.append(emp_id)

# to display the lists
print("Excellent performers : ", excellent)
print("Good performers : ", good)
print("Average performers : ", average)
print("Poor performers : ", poor)

''' 
Output:

Employees scoring above 80 :
EMP101
EMP104
EMP105
Number of employees needing improvement :  3
Top performer :  EMP105
Average performance score :  71.8
Excellent performers :  ['EMP101', 'EMP105']
Good performers :  ['EMP102', 'EMP104', 'EMP107']
Average performers :  ['EMP108', 'EMP110']
Poor performers :  ['EMP103', 'EMP106', 'EMP109']
''' 

