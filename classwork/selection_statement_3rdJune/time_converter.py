#program to convert time into corresponding hour, minute, second
second = int(input("enter time in seconds:"))
#check second is negative
if(second < 0):
    exit("time cannot be negative")
hour = 0
minute = 0
#converting number of second into hour
if(second >= 3600):
 hour = second//3600
 second = second % 3600
 #converting into minute
if(second >= 60):
    minute = second//60
    second = second % 60
print("Equivalent Time:", hour,"hour",minute,"minute",second,"second")