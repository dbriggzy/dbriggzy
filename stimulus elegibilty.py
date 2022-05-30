
#declare variables
income = int()
filing_type = str()

#ask user for their income and if they are married or single
income = int(input("Enter income:"))
filing_type = input("Are you a married joint tax filer?:")

#find out if the user qualifies for the full stimulus check
#married filers
if filing_type == "yes":
    if income < 150000:
        print("You are eligible for full stimulus payment")
    elif income < 160000:
        print("You are eligible for partial stimulus payment")
    else:
        print("You are not eligible for stimulus payment")
#single tax filers
else:
    if income < 75000:
        print("You are elibigle for full stimulus payment")
    elif income < 80000:
        print("You are eligible for partial stimulus payment")
    else:
        print("You are not eligible for stimulus payment")
