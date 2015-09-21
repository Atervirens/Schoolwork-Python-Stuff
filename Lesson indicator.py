week=0
carryon=True
while True: #insert programming below Try
    try:
        week=int(input("Input week 1 or 2: "))
        day=input("Input day (use capitalization): ")
        period=int(input("Input period: "))
        if week==1:
            if day=="Monday":
                if period==1:
                    print("Your lesson is maths, room M7.")
                elif period==2:
                    print("You have a free period.")
                elif period==3:
                    print("Your lesson is Computing, room Co2.")
                elif period==4:
                    print("Your lesson is a study period, room SFC2.")
                elif period==5:
                    print("Your lesson is physics, room S10.")
                else:
                    print("Error, invalid input was inputted.")
            elif day=="Tuesday":
                if period==1:
                    print("You have a lecture, main hall.")
                elif period==2:
                    print("Your lesson is a study period, room SFC2.")
                elif period==3:
                    print("Your lesson is physics, room E5.")
                elif period==4:
                    print("Your lesson is maths, M7.")
                elif period==5:
                    print("Your lesson is computing, room Co2.")
                else:
                    print("Error, invalid input was inputted.")
            elif day=="Wednesday":
                if period==1:
                    print("Your lesson is a study period, room SFC2.")
                elif period==2:
                    print("You have an EPQ meeting.")
                elif period==3:
                    print("Your lesson is physics, room S3.")
                elif period==4:
                    print("Your lesson is an elective, Lib1.")
                elif period==5:
                    print("Your lesson is an elective, room Co2.")
                else:
                    print("Error, invalid input was inputted.")
            elif day=="Thursday":
                if period==1:
                    print("Your lesson is maths, room M6.")
                elif period==2:
                    print("Your lesson is maths, room M7.")
                elif period==3:
                    print("Your lesson is computing, room Co2.")
                elif period==4:
                    print("You have a free period.")
                elif period==5:
                    print("Your lesson is physics, room S10.")
                else:
                    print("Error, invalid input was inputted.")
            elif day=="Friday":
                if period==1:
                    print("Your lesson is a study period, room SFC2.")
                elif period==2:
                    print("You have a free period.")
                elif period==3:
                    print("Your lesson is maths, room M6.")
                elif period==4:
                    print("Your lesson is computing, room Co2.")
                elif period==5:
                    print("Your lesson is physics, room S2.")
                else:
                    print("Error, invalid input was inputted.")
            else:
                print("Error, invalid input was inputted.")
        elif week==2:
            if day=="Monday":
                if period==1:
                    print("Your lesson is maths, room M7.")
                elif period==2:
                    print("You have a free period.")
                elif period==3:
                    print("Your lesson is Computing, room Co2.")
                elif period==4:
                    print("Your lesson is a study period, room SFC2.")
                elif period==5:
                    print("Your lesson is physics, room S10.")
                else:
                    print("Error, invalid input was inputted.")
            elif day=="Tuesday":
                if period==1:
                    print("You have a lecture, main hall.")
                elif period==2:
                    print("Your lesson is a study period, room SFC2.")
                elif period==3:
                    print("Your lesson is physics, room E5.")
                elif period==4:
                    print("Your lesson is maths, M7.")
                elif period==5:
                    print("Your lesson is computing, room Co2.")
                else:
                    print("Error, invalid input was inputted.")
            elif day=="Wednesday":
                if period==1:
                    print("Your lesson is a study period, room SFC2.")
                elif period==2:
                    print("You have an EPQ meeting.")
                elif period==3:
                    print("Your lesson is physics, room S3.")
                elif period==4:
                    print("Your lesson is an elective, Lib1.")
                elif period==5:
                    print("Your lesson is an elective, room Co2.")
                else:
                    print("Error, invalid input was inputted.")
            elif day=="Thursday":
                if period==1:
                    print("Your lesson is maths, room M6.")
                elif period==2:
                    print("Your lesson is maths, room M7.")
                elif period==3:
                    print("Your lesson is computing, room Co2.")
                elif period==4:
                    print("You have a free period.")
                elif period==5:
                    print("Your lesson is physics, room S10.")
                else:
                    print("Error, invalid input was inputted.")
            elif day=="Friday":
                if period==1:
                    print("Your lesson is a study period, room SFC2.")
                elif period==2:
                    print("You have a free period.")
                elif period==3:
                    print("Your lesson is maths, room M6.")
                elif period==4:
                    print("Your lesson is computing, room Co2.")
                elif period==5:
                    print("Your lesson is physics, room S2.")
                else:
                    print("Error, invalid input was inputted.")
            else:
                print("Error, invalid input was inputted.")
        else:
            print("Error, invalid input was inputted.")
                
    except ValueError: #Checks whether or not inputs are valid
        print("That isn't a valid input")

    carry=input("Reset? yes/no")

    if carry=="yes": #works with any string value
        carryon=True
    else:
        print("Insert termination message")
        carryon=False
        break #completely terminates program if termination option is chosen
    week=0
    carryon=True
    while True: #insert programming below Try
        try:
            week=int(input("Input week 1 or 2: "))
            day=input("Input day (use capitalization): ")
            period=int(input("Input period: "))
            if week==1:
                if day=="Monday":
                    if period==1:
                        print("Your lesson is maths, room M7.")
                    elif period==2:
                        print("You have a free period.")
                    elif period==3:
                        print("Your lesson is Computing, room Co2.")
                    elif period==4:
                        print("Your lesson is a study period, room SFC2.")
                    elif period==5:
                        print("Your lesson is physics, room S10.")
                    else:
                        print("Error, invalid input was inputted.")
                elif day=="Tuesday":
                    if period==1:
                        print("You have a lecture, main hall.")
                    elif period==2:
                        print("Your lesson is a study period, room SFC2.")
                    elif period==3:
                        print("Your lesson is physics, room E5.")
                    elif period==4:
                        print("Your lesson is maths, M7.")
                    elif period==5:
                        print("Your lesson is computing, room Co2.")
                    else:
                        print("Error, invalid input was inputted.")
                elif day=="Wednesday":
                    if period==1:
                        print("Your lesson is a study period, room SFC2.")
                    elif period==2:
                        print("You have an EPQ meeting.")
                    elif period==3:
                        print("Your lesson is physics, room S3.")
                    elif period==4:
                        print("Your lesson is an elective, Lib1.")
                    elif period==5:
                        print("Your lesson is an elective, room Co2.")
                    else:
                        print("Error, invalid input was inputted.")
                elif day=="Thursday":
                    if period==1:
                        print("Your lesson is maths, room M6.")
                    if period==2:
                        print("Your lesson is maths, room M7.")
                    if period==3:
                        print("Your lesson is computing, room Co2.")
                    if period==4:
                        print("You have a free period.")
                    if period==5:
                        print("Your lesson is physics, room S10.")
                    else:
                        print("Error, invalid input was inputted.")
                elif day=="Friday":
                    if period==1:
                        print("Your lesson is a study period, room SFC2.")
                    elif period==2:
                        print("You have a free period.")
                    elif period==3:
                        print("Your lesson is maths, room M6.")
                    elif period==4:
                        print("Your lesson is computing, room Co2.")
                    elif period==5:
                        print("Your lesson is physics, room S2.")
                    else:
                        print("Error, invalid input was inputted.")
                else:
                    print("Error, invalid input was inputted.")
            elif week==2:
                if day=="Monday":
                    if period==1:
                        print("Your lesson is maths, room M7.")
                    elif period==2:
                        print("You have a free period.")
                    elif period==3:
                        print("Your lesson is Computing, room Co2.")
                    elif period==4:
                        print("Your lesson is a study period, room SFC2.")
                    elif period==5:
                        print("Your lesson is physics, room S10.")
                    else:
                        print("Error, invalid input was inputted.")
                elif day=="Tuesday":
                    if period==1:
                        print("You have a lecture, main hall.")
                    elif period==2:
                        print("Your lesson is a study period, room SFC2.")
                    elif period==3:
                        print("Your lesson is physics, room E5.")
                    elif period==4:
                        print("Your lesson is maths, M7.")
                    elif period==5:
                        print("Your lesson is computing, room Co2.")
                    else:
                        print("Error, invalid input was inputted.")
                elif day=="Wednesday":
                    if period==1:
                        print("Your lesson is a study period, room SFC2.")
                    elif period==2:
                        print("You have an EPQ meeting.")
                    elif period==3:
                        print("Your lesson is physics, room S3.")
                    elif period==4:
                        print("Your lesson is an elective, Lib1.")
                    elif period==5:
                        print("Your lesson is an elective, room Co2.")
                    else:
                        print("Error, invalid input was inputted.")
                elif day=="Thursday":
                    if period==1:
                        print("Your lesson is maths, room M6.")
                    elif period==2:
                        print("Your lesson is maths, room M7.")
                    elif period==3:
                        print("Your lesson is computing, room Co2.")
                    elif period==4:
                        print("You have a free period.")
                    elif period==5:
                        print("Your lesson is physics, room S10.")
                    else:
                        print("Error, invalid input was inputted.")
                elif day=="Friday":
                    if period==1:
                        print("Your lesson is a study period, room SFC2.")
                    elif period==2:
                        print("You have a free period.")
                    elif period==3:
                        print("Your lesson is maths, room M6.")
                    elif period==4:
                        print("Your lesson is computing, room Co2.")
                    elif period==5:
                        print("Your lesson is physics, room S2.")
                    else:
                        print("Error, invalid input was inputted.")
                else:
                    print("Error, invalid input was inputted.")
            else:
                print("Error, invalid input was inputted.")
                
        except ValueError: #Checks whether or not inputs are valid
            print("That isn't a valid input")

        carry=input("Reset? yes/no")

        if carry=="yes": #works with any string value
            carryon=True
        else:
            print("Insert termination message")
            carryon=False
            break #completely terminates program if termination option is chosen

