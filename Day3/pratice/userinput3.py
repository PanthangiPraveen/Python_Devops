age = int(input("Please enter your age "))

while age <= 0:
    print("invalid age please provide age grater then zero(0) ")
    age = int(input("please enter your age  "))
    
 # Now check voting eligibity   
if age < 18:
    print(" your age is not eligibil to cast the vote. ")
    print("the eligible age to cast the vote is grater then equal to 18")
elif age >= 18:
    print("Yes your are eligible to cast the vote. please processed. ")