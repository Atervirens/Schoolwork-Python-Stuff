value=0
carryon=True
while True: #insert programming below Try
    try:

    except ValueError: #Checks whether or not inputs are valid
        print("Insert error message here)

    carry=input("Insert true/false query. yes/no")

    if carry=="yes": #works with any string value
        carryon=True
    else:
        print("Insert termination message")
        carryon=False
        break #completely terminates program if termination option is chosen
