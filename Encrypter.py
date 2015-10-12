alphabet='abcdefghijklmnopqrstuvwxyz'

alinput=['encrypt', 'decrypt', 'end']

def checkinput(): #Function to check input for validity
    while True:
        deci=input("Encrypt, decrypt or end? (encrypt/decrypt/end) ")
        if deci in alinput:
            return deci
        else:
            print("encrypt, decrypt and end only.")
def encrypt(key): #encryption function

    plain=input("Input message (don't capitalize or punctuate): ")

    citext=''

    for hold in plain: 
        pos=alphabet.index(hold)
        pos+=key

        if hold in alphabet:
            if pos>=26:
                pos=pos%26
            citext+=alphabet[pos]
        else:
            citext+=hold
            
    print("Your message is now '", citext, "'.")

    
def dencrypt(key): #decryption function
    citext=input("Input message (don't capitalize or punctuate): ")

    plain=''

    for pi in citext:
        hos=alphabet.index(pi)
        hos-=key
        if pi in alphabet:
            if hos>=26:
                hos=hos%26
            plain+=alphabet[hos]
        else:
            plain+=pi
        [hos]
    print("Your message is now '", plain, "'.")
keysize=26
def keysizer(): #asks for keysizes and confirms that it's an integet between or equal to 1-26
    while True:
        inp=input("Input input between 1 and 26: ")
        try:
            inp=int(inp)
            if inp>26 or inp<1:
                
              
                print("Keysize doesn't fit")
            else:
                print("Your keysize is: ", inp)
                return inp
        except ValueError:
            print("That's not a number")
            
deci=checkinput()
carryon=True
while carryon:
    
    if deci=="encrypt":
        
        key=keysizer()
        plain=encrypt(key)
        deci=checkinput()
        
    if deci=="decrypt":
        
        key=keysizer()
        citext=dencrypt(key)
        deci=checkinput()
    if deci=="end":
        print("Ending program")
        carryon=False
        break
    
        
    
            

