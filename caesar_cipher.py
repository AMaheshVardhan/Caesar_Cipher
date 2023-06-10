alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#direction=input("Hey,Type 'encode' to encrypt , 'decode' to decrypt\n")
text=input("Enter your message\n").lower()
shift=int(input("Enter the shift number\n"))
def encrypt(plain_text,shift_amount):
        cipher_text=""
        for letter in plain_text:
             position=alphabet.index(letter)
             new_position=position+shift_amount
             new_letter=alphabet[new_position]
             cipher_text+=new_letter
        print(f"The encoded text is {cipher_text}") 
def decrypt(plain_text,shift_amount):
           cipher_text=""
           for letter in plain_text:
               position=alphabet.index(letter)
               new_position=position-shift_amount
               new_letter=alphabet[new_position]   
               cipher_text+=new_letter  
           print(f"The Decoded Text is {cipher_text}")
choice=int(input("1->Encode\n2->Decode\n"))
if choice==1:
       encrypt(text,shift)
else:
       decrypt(text,shift)                 
            
     
           