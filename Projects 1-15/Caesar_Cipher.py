print('''
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88           
''')
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
continued = "yes"

def encrypt(text, shift):
    encode_letter = ""
    for letter in text:
        if letter not in alphabet:
            encode_letter += letter
        else:
            letter_index = (alphabet.index(letter) + shift) % 26
            encode_letter += alphabet[letter_index]
    print(f"Encoded result: {encode_letter}")

def decrypt(text, shift):
    decode_letter = ""
    for letter in text:
        if letter not in alphabet:
            decode_letter += letter
        else:
            letter_index = (alphabet.index(letter) - shift) % 26
            decode_letter += alphabet[letter_index]
    print(f"Decoded result: {decode_letter}")

while not continued == "no":
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction == "encode":
            break
        elif direction == "decode":
            break
        else:
            print("Wrong insert")

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        encrypt(text,shift)
    else:
        decrypt(text, shift)

    continued = input("\nDo you want to do again? (digit 'yes' or 'no')\n")
    if continued == "yes":
        continued == "yes"
    else:
        continued == "no"
input("\npress ENTER for finish")






