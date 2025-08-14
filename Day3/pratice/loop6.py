fruits = {
    "apple" : "red",
    "banana" : "yellow",
    "mango" : "pink",
    "orange" : "orange",
    "waterMelon" : "green"
    
}
for fruit, colour in fruits.items():
    if colour == "green":
        print(f"{fruit.capitalize()} is so delicious and {colour.upper()} in colour")