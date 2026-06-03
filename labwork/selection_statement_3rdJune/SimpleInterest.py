principle = int(input("enter principle amount(in rs):"))
if(principle < 0):
    exit("principle cannot be negative")
rate = int(input("enter the rate(in percentage):"))
if(rate < 0):
    exit("rate cannot be negative")
time = int(input("enter the time(in years):"))
if(time < 0):
    exit("time cannot be negative")

si = ( principle * rate * time )/100
print("simple interest",si,"rs")