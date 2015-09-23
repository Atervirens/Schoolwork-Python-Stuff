carryon=True
while True:
    integer=0
    positive=0
    negative=0
    even=0
    odd=0
    try:
        numin=int(input("(Type Terminate to end program) \nPlease input an integer: "))
        while numin !=-999:
            integer=integer+1
            if numin>0:
                positive=positive+1
            if numin<0:
                negative=negative+1
            if numin%2==0:
                even=even+1
            if numin==str("Terminate"):
                break
            else:
                odd=odd+1
            print("Number of inputs=", integer, "\n Number of positive numbers=", positive, "\n Number of negative numbers=", negative, "\n Number of even numbers=", even, "\n Number of odd numbers=", odd)
            numin=int(input("(Type Terminate to end program) \nPlease input an integer: "))
        
    
    except ValueError:
        
        carry=input("Try again? yes/no ")
    


    if carry=="yes":
        carryon=True
    else:
        print("Terminating program.")
        carryon=False
        break
