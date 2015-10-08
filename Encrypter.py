alphabet='abcdefghijklmnopqrstuvwxyz '
shifted='defghijklmnopqrstuvwxyz abc'
alinput=['encrypt', 'decrypt', 'end']

def checkinput(): #Function to check input for validity
    while True:
        deci=input("Encrypt, decrypt or end? (encrypt/decrypt/end) ")
        if deci in alinput:
            return deci
        else:
            print("encrypt or decrypt only.")
           
deci=input("Encrypt, decrypt or end? (encrypt/decrypt/end) ")
carryon=True
while carryon:
    
    if deci=="encrypt":
        
        plain=input("Input message (don't capitalize or punctuate): ")

        citext=''

        for hold in plain: #caesar encryption program
            pos=alphabet.index(hold)
            citext=citext+shifted[pos]
        print("Your message is now '", citext, "'.")
        deci=checkinput()
        
    if deci=="decrypt":
        
        
        citext=input("Type encrypted message (don't capitalize or punctuate): ")
        plain=''
        for pi in citext: #decryption program
            hos=shifted.index(pi)
            plain=plain+alphabet[hos]
        print("Your message is '", plain, "'.")
        deci=checkinput()
    if deci=="end":
        print("Ending program")
        carryon=False
        break
    
        
    
            

