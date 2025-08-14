age = int(input("enter you age  "))

if age < 18 :
    print("your are age is less than eligibility")
elif age == 18:
    print("your age is exact equal to eligiblity so try next year")
elif age > 18:
    print("your are eligible ")
else:
    print("invalide")