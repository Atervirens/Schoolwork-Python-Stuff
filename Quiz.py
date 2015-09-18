answer=0
carryon=True
while True:        
    try:
        score=0
        answer=input("What is the capital of France? (Use capitalization and correct spelling.): ")
        if answer=="Paris":
            
            score=score+1 #Increases score by one point.

            print("Correct! Your score is ", score, ".", sep="")
        else:
            print("Incorrect, the answer was 'Paris'. Your score is ", score, ".", sep="")
        answer=int(input("What is 5674 + 9880?: ")) #Values can be overwritten by using in another input
        if answer==5674+9880: #Comparisons can be made with a calculation
            score=score+1
            print("Correct! Your score is ", score, ".", sep="")
        else:
            print("Incorrect, the answer was '15554'. Your score is ", score, ".", sep="")
        answer=int(input("What is 5674 - 9880?: "))
        if answer==5674-9880:
            score=score+1
            print("Correct! Your score is ", score, ".", sep="")
        else:
            print("Incorrect, the answer was '-4206'. Your score is ", score, ".", sep="")
        answer=int(input("What is the result of 5674/9? (Use whole numbers): "))
        if answer==630:
            score=score+1
            print("Correct! Your score is ", score, ".", sep="")
        else:
            print("Incorrect, the answer was '630'. Your score is ", score, ".", sep="")
        answer=int(input("What is the remainder of 5674/9?: "))
        if answer==4:
            score=score+1
            print("Correct! Your score is ", score, ".", sep="")
        else:
            print("Incorrect, the answer was '4'. Your score is ", score, ".", sep="")
        answer=int(input("What year did the first Doctor Who episode air? "))
        if answer==2005:
            score=score+1
            print("Correct! Your score is ", score, ".", sep="")
        else:
            print("Incorrect, the answer was '2005'. Your score is ", score, ".", sep="")
        if score <=1:
            print("Your score is ", score,", there's always next time!")
        else:
            print("Congratulations, your score is: ", score,)
                   
        
    except ValueError:
        print("Error, that input is invalid.")

    carry = input("Try again? yes/no ")

    if carry=="yes":
        carryon=True
    else:
        print("Quiz terminated.")
        carryon=False
        break

