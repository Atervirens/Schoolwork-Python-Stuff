carryon=True
while True:
    try:
        numin=int(input("Please input an integer: "))
        integer=0
        positive=0
        negative=0
        even=0
        odd=0
    
    except ValueError:
        print("Input is not valid.")
    carry=input("Reset program? yes/no ")
    while numin !=<-999:
        integer=integer+1
        if numin>0:
            positive=positive+1
        if numin<0:
            negative=negative+1
        if numin%2==0:
            even=even+1
        else:
            odd=odd+1
        print("Number of inputs=", integer, ", number of positive numbers=", positive, ", number of negative numbers=", negative, ", number of even numbers=", even, ", and number of odd numbers=" odd)


    if carry=="yes":
        carryon=True
    else:
        print("Terminating program.")
        carryon=False
        break
