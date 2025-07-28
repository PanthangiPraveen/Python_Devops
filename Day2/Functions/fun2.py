def calculator():
    
    while True:
        try:
            num1 = float(input("Please enter the number1 "))
            num2 = float(input("Please enter the number2 "))
            break
        except ValueError:
            print("Ooops one of these are not valide number, so please enter only numbers")
            
    
calculator()  
    