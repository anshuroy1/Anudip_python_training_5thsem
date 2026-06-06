# create a dictionary to store students data
#to create a dictionary to store student's data 
students={'std101':"Akash",'std102':"abhinav",'std103':"anil",'std104':"Rahul"}

#to display data 
print("Student details : ")
print(students)

print("------------------")

#to update the record of student whose roll no is std103
students['std103']="Nishant"

#to update the record of student whose roll no is std105
students['std105']="Rakesh"

print("students detail :")
print(students)

print("------------------------------")
for x in students:
    print(x ,"->",students[x])