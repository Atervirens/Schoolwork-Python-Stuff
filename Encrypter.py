alphabet='abcdefghijklmnopqrstuvwxyz'

alinput=['encrypt', 'decrypt', 'end']
keysize=26

def checkinput():
    while True:
        deci=input("Encrypt, decrypt or end? (encrypt/decrypt/end) ")
        if deci in alinput: #checks input for invalid inputs
            if deci=="encrypt":
                return deci
            if deci=="decrypt":
                return deci
            if deci=="end":
                print("ending")
                carryon=False
                break
            else:
                print("encrypt, decrypt and end only.")
            
def translate(): #encryption function
    carryon=True
    while carryon:
        deci=checkinput()
    
        text=input("Input message (don't capitalize or punctuate): ")
        
        key=keysizer()
        if deci=="decrypt":
            key=-key

        translate=''

        for hold in text:
            if hold.isalpha():
                pos=alphabet.index(hold)
                pos+=key
                if pos>=keysize:
                    pos=keysize%25
                if pos <0:
                    pos=keysize+pos
                translate+=alphabet[pos]
            else:
                translate+=hold
                    
                    
        print("Your message is now '", translate, "'.")
        

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
            


encrypt=translate()
    
        
    
            

