fruits = {
    "apple" : "red",
    "banana" : "yellow",
    "mango" : "pink",
    "orange" : "orange",
    "waterMelon" : "green"
    
}

for index,(fruit,colour) in enumerate(fruits.items(),start=1):
    print(f"{index} {fruit.capitalize()} is {colour.upper()} colour")