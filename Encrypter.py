alphabet='abcdefghijklmnopqrstuvwxyz '
shifted='defghijklmnopqrstuvwxyz abc'
alinput=['encrypt', 'decrypt', 'end']

def checkinput(): #Function to check input for validity
    while True:
        deci=input("Encrypt, decrypt or end? (encrypt/decrypt/end) ")
        if deci in alinput:
            return deci
        else:
            print("encrypt, decrypt and end only.")
def encrypt(): #encryption function

    plain=input("Input message (don't capitalize or punctuate): ")

    citext=''

    for hold in plain: 
        pos=alphabet.index(hold)
        citext=citext+shifted[pos]
    print("Your message is now '", citext, "'.")
def dencrypt(): #decryption function
    citext=input("Input message (don't capitalize or punctuate): ")

    plain=''

    for pi in citext:
        hos=shifted.index(pi)
        plain=plain+alphabet[hos]
    print("Your message is now '", plain, "'.")
keysize=26
def keysizer(): #asks for keysizes and confirms that it's an integet between or equal to 1-26
    while True:
        inp=input("Input input between 1 and 26: ")
        try:
            inp=float(inp)
            if inp>26 or inp<1:
                
              
                print("Keysize doesn't fit")
            else:
                print("Your keysize is: ", inp)
                return inp
        except ValueError:
            print("That's not a number")
deci=input("Encrypt, decrypt or end? (encrypt/decrypt/end) ")
carryon=True
while carryon:
    
    if deci=="encrypt":
        

        plain=encrypt()
        deci=checkinput()
        
    if deci=="decrypt":
        
        citext=dencrypt()
        deci=checkinput()
    if deci=="end":
        print("Ending program")
        carryon=False
        break
    
        
    
            

