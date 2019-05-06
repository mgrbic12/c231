#affine cipher
#Lab 2, Max Grbic, March 1, 2019

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
print("1.Lab2: This will decrypt using an affine cipher(key1=17, key2=8).")
print("Encrypted message 1: TB242520C48GVV4S,0247J,04TB245,JTBZ")
print("-" * 25)

userC = input("Enter a message to decrpyt (A-Z): ")
userC = userC.upper()
print("-" * 25)
for thing in userC:
    decrypt = (((alphabet.index(thing) - 8) * 17) % len(alphabet))
    decodeNum.append(decrypt)
for piece in decodeNum:
    decodeText.append(alphabet[piece])
for let in decodeText: 
    print(let, end='')
    
################
print()
print("-" * 25)
print("-" * 25)
print("2.Lab2: This will decrypt using an affine cipher(key1=41, key2=30).")
print("Encrypted message 2: X0N30NL8Q98G4N1T0G8I4M83QNR8WR8D  .8WR8IQNLXWRYLQR,8WR1W4R498X08I4M84PPQWRL0182XW0Z8QZ8LX08R0I82NGPLQ4R4TGLW28KRWL,8SW 9")
print("-" * 25)

encodeNum2 = []
cipherText2 = []
decodeNum2 = []
decodeText2 = []

userC2 = input("Enter a message to decrpyt (A-Z): ")
userC2 = userC2.upper()
print("-" * 25)
for thing in userC2:
    decrypt = (((alphabet.index(thing) - 30) * 41) % len(alphabet))
    decodeNum2.append(decrypt)
for piece in decodeNum2:
    decodeText2.append(alphabet[piece])
for let in decodeText2: 
    print(let, end='')

##################

print()
print("-" * 25)
print("-" * 25)
print("3.Lab2: This will decrypt using an affine cipher(key1=25, key2=39).")
print("Encrypted messge 3:!QR7LVTR7TQ7T1R3LVGX2T R73!TQ3TRN;7R8L QRLX2RLOR2ETRNL 5RLQR3 DG2L;Q;0D:!QJR2ETRJT V;QRTQ!JV;RV;3E!QTW")
print("-" * 25)

encodeNum3 = []
cipherText3 = []
decodeNum3 = []
decodeText3 = []

userC3 = input("Enter a message to decrpyt (A-Z): ")
userC3 = userC3.upper()
print("-" * 25)
for thing in userC3:
    decrypt = (((alphabet.index(thing) - 39) * 25) % len(alphabet))
    decodeNum3.append(decrypt)
for piece in decodeNum3:
    decodeText3.append(alphabet[piece])
for let in decodeText3: 
    print(let, end='')
