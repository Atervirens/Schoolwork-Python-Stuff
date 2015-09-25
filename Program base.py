def inputcheck(value): #Function checks if the input is a number or not
    try:
        value=float(value)
        return True
    except ValueError:
        return False
    
carryon=True
while True: #insert programming below while True
    value=input("Input a value: ")
    if inputcheck(value)==True:
        value=float(value)
        print(value)
    else:
        print("Invalid input.")
        value=input("Input a value: ")
    

    carry=input("Insert true/false query. yes/no ")

    if carry=="yes": #works with any string value
        carryon=True
    else:
        print("Insert termination message ")
        carryon=False
        break #completely terminates program if termination option is chosen
