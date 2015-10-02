alphabet='abcdefghijklmnopqrstuvwxyz '
shifted='defghijklmnopqrstuvwxyz abc'
carryon=True
while True:
    while True:
        deci=input("Encrypt or decrypt? (encrypt/decrypt) ")
        if deci=="encrypt":
            
            plain=input("Input message (don't capitalize or punctuate): ")

            citext=''

            for hold in plain: #caesar encryption program
                pos=alphabet.index(hold)
                citext=citext+shifted[pos]
            print("Your message is now '", citext, "'.")
            
        elif deci=="decrypt":
            
            
            citext=input("Type encrypted message (don't capitalize or punctuate): ")
            plain=''
            for pi in citext: #decryption program
                hos=shifted.index(pi)
                plain=plain+alphabet[hos]
            print("Your message is '", plain, "'.")
            
        else:
            print("encrypt or decrypt only.")
            
            carryon=False
        carry=input("Use again? encrypt/decrypt/no ")
        if carry=="encrypt": #works with any string value
            carryon=True
            plain=input("Input message (don't capitalize or punctuate): ")

        elif carry=="decrypt":
            carryon=True
            citext=input("Type encrypted message (don't capitalize or punctuate): ")
        elif carry=="no":
            print("Terminating program.")
            break 
            
        else:
            print("encrypt, decrypt or no only.")
            carry=input("Use again? encrypt/decrypt/no ")

