from os import name,system


def banner():           ##Function to show banner
    
    print("\033[1;32;40m+-+-+-+-+-+-+-+-+-+-+-+-+  +-+-+-+-+")
    print("\033[1;31;40m|C|r|y|p|t|o|g|r|a|p|h|y|  |T|o|o|l|")
    print("\033[1;32;40m+-+-+-+-+-+-+-+-+-+-+-+-+  +-+-+-+-+\n")
   


    print("\033[1;35;40m---- XXX Encryption is not a crime XXX---- ")
    print("\033[1;35;40m---- XXX      By rubbish     XXX---- \n\n")
    print("\033[0;37;40m")
def clear():           ##function to clear screen according to O.S.
    if name=="nt":
       system("cls")
    else:
       system("clear")

def menu():
    print("Encryption Methods\n")
    print("1. Ceasar Cipher")
    print("2. Vigenere Cipher")
    print("3. Rot 13 cipher")
    print("4. Rot 47 cipher")
    
    print("\nDecryption Methods\n")
    print("5. Ceasar Cipher decryption")
    print("6. Vigenere  Cipher decryption")
    print("7. Rot 13 decryption")
    print("8. Rot 47 decryption")
    print("\nEnter your choice")
    choice=0
    try:
        choice=int(input())
    except Exception as error:    
        clear()
        print("Error !!, pls enter the correcy choice")
        exit(0)
    try:            
        if choice == 1:
                ceasar_cipher()
        elif choice == 2:
                vigenere_cipher() 
        elif choice == 5:
                ceasar_decrypt()
        elif choice == 6:
                vigenere_decrypt()
        elif choice == 3:
                rot_13()
        elif choice == 7:
                rot_13_decrypt()
        elif choice == 4:
                rot_47()
        elif choice == 8:
                rot_47_decrypt()
    except Exception as e:
        print(e)

def ceasar_cipher():                ## Ceasar cipher (symmetric)
    print("\n>>> Enter the mesage to encrypt using ceasar")
    message=input()
    print("\n>>> Enter the key in interger value")
    key=0
    try:
        key=int(input())
    except Exception as error:
        clear()
        print("Error !!, pls enter key in number only")
        exit(0)
    key=(key%26)
    msg=list(message)
    message=""
    for i in msg:
        if(i.isalpha()):
            if(ord(i)>=97 and ord(i)<=122):
                value=ord(i)+key
                if value>122:
                    value=value-122
                    i=chr(96+value)
                else:
                    i=chr(value)
                message+="".join(i)
            elif(ord(i)>=65 and ord(i)<=90):
                value=ord(i)+key
                if value>90:
                    value=value-90
                    i=chr(64+value)
                else:
                    i=chr(value)
                message+="".join(i)

        else:
            message+="".join(i)
    print("\n### Ceasar ciphered encrypted text is ")
    print(message)

def ceasar_decrypt():           ##ceasar decrypt
    print("\n>>> Enter the ceasar cipher message to decrypt")
    message=input()
    print("\n>>> Enter the key of ceaser cipher message in interger value")
    key=0
    try:
        key=int(input())    
    except Exception as error:    
        clear()
        print("Error !!, pls enter key in number only")
        exit(0)
    
    key=(key%26)
    msg=list(message)
    message=""
    for i in msg:
        if(i.isalpha()):
            if(ord(i)>=97 and ord(i)<=122):
                value=ord(i)-key
                if value<97:
                    value=97-value
                    i=chr(123-value)
                else:
                    i=chr(value)
                message+="".join(i)
            elif(ord(i)>=65 and ord(i)<=90):
                value=ord(i)-key
                if value<65:
                    value=65-value
                    i=chr(91-value)
                else:
                    i=chr(value)
                message+="".join(i)
        else:
            message+="".join(i)
    print("\n### Decrypted plain text from ceasar cipher is ")
    print(message)
 
def vigenere_cipher():      
    print("\n>>> Enter the mesage to encrypt using vigenere cipher")
    message=input()                                                             
    print("\n>>> Enter the key (only alphabet character [ascii between a-z and A-Z] and length greater than 1")  
    key=input()
    try:
        for x in key:
            if (x.isalpha()):
                pass
            else:
                raise Exception("Invalid characters in key")
    except Exception as e:
        clear()
        print(e)
        exit(0)
        
    msg=list(message)
    k=list(key)
    length=len(key)
    counter=0
    message=""
    for i in msg:
        if(i.isalpha()):
            if(i.isupper()):
                value= (ord(i)+ord(k[counter%length].upper()))%26
                counter+=1
                i=chr(65+value)
                message+="".join(i)
            else:
                i=i.upper()
                value= (ord(i)+ord(k[counter%length].upper()))%26    
                counter+=1
                i=chr(65+value)
                message+="".join(i.lower())
                
        else:
            message+="".join(i)

    print("\n### The vigenere ciphered message is")
    print(message)

def vigenere_decrypt():
    print("\n>>> Enter the encrpted message ")
    message=input()
    print("\n>>> Enter the key (only alphabet character [ascii between a-z and A-Z] and length greater than 1")  
    key=input()
    try:
        for x in key:
            if (x.isalpha()): 
                pass
            else:
                raise Exception("Invalid characters in key")     
    except Exception as e:
        clear()
        print(e)
        exit(0)
    msg=list(message)
    k=list(key)
    length=len(key)
    counter=0
    message=""
    for i in msg:
        if(i.isalpha()):
            if(i.isupper()):
                value= (ord(i)-ord(k[counter%length].upper()) + 26)%26
                counter+=1
                i=chr(65+value)
                message+="".join(i)
            else:    
                i=i.upper()
                value= (ord(i)-ord(k[counter%length].upper()) +26)%26
                counter+=1
                i=chr(65+value)
                message+="".join(i.lower())
                
        else:
            message+="".join(i)
    print("\n### Decrypted plaintext is")
    print(message)

def rot_13():
    print("\n>>> Enter the mesage to encrypt using rot13")
    message=input()
    key=13
    msg=list(message)
    message=""
    for i in msg:
        if(i.isalpha()):
            if(ord(i)>=97 and ord(i)<=122):
                value=ord(i)+key
                if value>122:
                    value=value-122
                    i=chr(96+value)
                else:
                    i=chr(value)
                message+="".join(i)
            elif(ord(i)>=65 and ord(i)<=90):
                value=ord(i)+key
                if value>90:
                    value=value-90
                    i=chr(64+value)
                else:
                    i=chr(value)
                message+="".join(i)

        else:
            message+="".join(i)
    print("\n### Ceasar rot13 encrypted text is ")
    print(message)

def rot_13_decrypt():
    print("\n>>> Enter the encrypted message ")
    message=input()
    key=13
    msg=list(message)
    message=""
    for i in msg:
        if(i.isalpha()):
            if(ord(i)>=97 and ord(i)<=122):
                value=ord(i)-key
                if value<97:
                    value=97-value
                    i=chr(123-value)
                else:
                    i=chr(value)
                message+="".join(i)
            elif(ord(i)>=65 and ord(i)<=90):
                value=ord(i)-key
                if value<65:
                    value=65-value
                    i=chr(91-value)
                else:
                    i=chr(value)
                message+="".join(i)
        else:
            message+="".join(i)
    print("\n### Decrypted plain text is ")
    print(message)

def rot_47():
    print("\n>>> Enter the  message to encrypt using rot 47")
    message=input()
    key=47
    msg=list(message)
    message=""
    for i in msg:
        if (ord(i)>=33 and ord(i)<=126):
            value=ord(i)+key
            if value>126:
                value=value-126
                i=chr(32+value)
            else:
                i=chr(value)
            message+="".join(i)
            
        else:
            message+="".join(i)
            
    print("\n### Encrypted rot 47 text is")
    print(message)

def rot_47_decrypt():
    print("\n>>> Enter the encrypted message")
    message=input()
    key=47     
    msg=list(message)
    message=""
    for i in msg:
        if (ord(i)>=33 and ord(i)<=126):
            value=ord(i)-key
            if value<33:
                value=33-value
                i=chr(127-value)
            else:
                i=chr(value)
            message+="".join(i)
            
        else:
            message+="".join(i)
    print("\n### Decrypted plain text is")
    print(message) 

if __name__=="__main__":
    banner()
    menu()
