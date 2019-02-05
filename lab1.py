#affine cipher
#Lab 1, Max Grbic, January 30, 2019

#List of all potential characters to be used
letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbol = [",", ".", " ", ";", ":", "!"]
alphabet = letter + digits + symbol

encodeNum = []
cipherText = []
decodeNum = []
decodeText = []

#the code automatically accepts the user input as upper caser
#if needed, this could be changed and an invalide statement could be returned to the user when an invalide character is user
print("This program will encrpyt/decrypt an affine cipher(key1=5, key2=11).")
print("All user inputs are formatted to accept lowercase and handle them like upper case.")
print("-" * 25)
#Obtain user message
choice = input("Would you like to encrypt or decrypt (E/D): ")
choice = choice.upper()

if choice == "E" or choice == "ENCRYPT":
    userText = input("Enter a message to encrypt(A-Z): ")
    userText = userText.upper()
    print("-" * 25)

#loop through message and determine if the character is valid

    for item in userText:
        if item in alphabet:
            encoded = (((alphabet.index(item) * 5) + 11) % len(alphabet))
            encodeNum.append(encoded)
        else:
            print("Invalid character!")

    for num in encodeNum:
        cipherText.append(alphabet[num])

    print("This is your encrpyted message:")
    for char in cipherText:
        print(char, end='')

if choice == "D" or choice == "DECRYPT":
    userC = input("Enter a message to decrpyt (A-Z): ")
    userC = userC.upper()
    print("-" * 25)
    for thing in userC:
        decrypt = (((alphabet.index(thing) - 11) * 17) % len(alphabet))
        decodeNum.append(decrypt)
    for piece in decodeNum:
        decodeText.append(alphabet[piece])
    for let in decodeText: 
        print(let, end='')



        





