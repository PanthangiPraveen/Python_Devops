# Task 1: Declare variables for your name, age, and favorite language
name = "Praveen"
age = 34
favorite_language = "Telugu"

# Task 2: Create a constant for max login attempts

MAX_LOGIN = 10

# Task 3: Write a comment explaining what your code does

'''This code explaining 
the varialbe_constructions,DataTypes,InputOutput and 
syntax_indentation'''

# Task 4: Use input() to get user's name and age, then print a greeting
# Task 5: Use f-string to format a message

name = input("what is your name  ")
age = int(input("what is your age  "))
print(f"Hello Good Morning {name}" )

# Task 6: Write an if-else block to check if age > 18
age = int(input("what is your age  "))

if age < 18:
    print("Minor")
elif 18 <= age < 60:
    print("Audult")
else:
    print("Senior")