#enter the electricity units that user consumed 
consumed_units=int(input("enter the consumed elecricity units :"))

#validate the consumed units if it is negative

if(consumed_units < 0):
    print("consumed units cannot be negative")

    #display the consumed units

print("units consumed",consumed_units)

#checking whether the consumption is high , moderate and low 
#also calculating the total bill of the user 

if(consumed_units<=100):

    bill=consumed_units*5

   
elif(consumed_units<=200):

    bill=100*5+((consumed_units-100)*7)

else:
    bill=(100*5)+(100*7)+((consumed_units-200)*10)


# Add 10% surcharge if bill exceeds ₹5000
if bill > 5000:
    surcharge = bill * 10 / 100
    bill = bill + surcharge

# Display final bill
print("Final Bill =", bill)