#Max Grbic
#CSCI-C231
#Lab4 : Vigenere cipher decryption
#correct decryption, something is wrong with the way the PDF copy and paste into the program, formatting issues maybe.
#IN 1938, THE JAPANESE REPLACED THE RED MACHINE WITH THE TYPE B MACHINE, WHICH CAME TO BE KNOWN AS PURPLE. IT TOOK A MUCH LARGER TEAM UNDER FRANK ROWLETTS DIRECTION EIGHTEEN MONTHS TO BREAK INTO THIS SYSTEM; THE FIRST TRANSLATION WAS PRODUCED IN SEPTEMBER 1940. IT CAME OUT ONE WEEK AFTER A CRUCIAL KEY TO THE PUZZLE HAD BEEN SUGGESTED BY THE GENEVIEVE GROTJAN, AN SIS JUNIOR CRYPTANALYST. AN ANALOG WAS CONTRUCTED UNDER THE DIRECTION OF THE LE O ROSEN, AN SIS ENGINEER, ANd WHEN IT WAS OPERATIONAL, THE US HAD ACCESS TO ALL OF THE HIGH LEVEL JAPANESE-DIPLOMATIC COMMUNICATIONS. MR. ROWLETT S AWARDS INCLUDE NSA EXCEPTIONAL CIVILIAN SERVICE AWARD, THE NATIONAL INTELLIGENCE DISTINGUISHED SERVICE MEDAL, THE PRESIENTS AWARD FOR DISTINGUISHED FEDERAL CIVILIAN SERVICE, THE NATIONAL SECURITY MEDAL, AND IN 1964 CONGRESS AWARDED HIM 100,00 FOR HIS INVENTIONS HELD SECRETE BY THE GOVERNMENT.

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,. ;:!'
def main():
    chosen_keyword = 'I231S'
    chosen_type='decrypt'
    ctext = """Q!ZML.UXX.P6Z,SX2A5,MYE57T255VEF,5OZ66X4I4,95MYJ9.PYG8WEFLAWE3Z;SK9.:WCY
J80K9Z3SU6ZE6E37X2VAJ:OIEZA ZB:5NE,GX.WA;XSE:H3ZE;3CYMDZEWI:ZF5L6EXXZ2A.
OZAJ W1FFXVQD73.QAAXWQ8,EWM!Z;6VF,DO1AZ29M2;X0VFBX.P,FX,6EG54FYG8WE7.C,1
YGCSVE:1.QAAX:IEZA9W5H3WLY.:O06CEWU37CO9VRLNE,GXUI:7X6V6ZHWM Z1X16EXSE4E
FUQ2:X2MKZE6EF,5OXGMK3MY,1VE3755EEH7YMEG5VE3LXYM!7G0MH7XYZAG,SVWZ15EE.DO
RGA96ZY5CAXF3:STKFENE2AXSV2:!YEI3DOKAAD.ZG5EWLYH:VMDZEZMY699M4G96VYB6OT6
BX9WE7:ME2AX,QEZ55O,A5WZWZ15LYJ8WVY.EO42FX6X6E1.QAA13CYG8WEGFXZI5Z1UK6FD
O1AZ13TYB6O197XZQ8,X3MH7 OR2C15ME7XVQB:!4IF.3OKA!; V,51.QAADNE:EWOZAJ W1F
FXS42E4,E,A33257X502Z5!K6CE0W!3 OK,I93Q2AX,MDI9UMY3HSZ5XX.P6Z:S1,B:STY.:.
M;:9YM!55OL,FE0V8H9,P66X,MDI9UMY!5VI;XX.P6ZA9ME.4WVFFXS42E4ONAEXVQEG95OG.
DZM5Z6WL6E13E4.G0T,3:O06EG0K6XX.P6Z:S1,B:STYF5U2D.EAE:74STWZ15LY.:O9VTPOK
AA79MEFXS42E4WLY,94ENNLM8MNXXWDZ800Y.:;M!G96VEZ8WT5ZDWKD7EOJKZEZMY9!;MDA;
WVFY"""
    #ctext = """""" #(enter correct ciphertext|switch # comments with ctext)
    if chosen_type == 'encrypt':
        translated = encrypt(chosen_keyword, ctext)
        print('--encrypted plaintext--')
    if chosen_type == 'decrypt':
        translated=decrypt(chosen_keyword, ctext)
        print('--decrypted ciphertext--')
    print(translated)
def encrypt(key,message):
    return translate(key,message,'encrypt')
def decrypt(key,message):
    return translate(key,message,'decrypt')
def translate(key,message,modeType):
    translated=[]
    Index = 0
    key = key.upper()
    for symbol in message:
        num = alphabet.find(symbol.upper())
        if num != -1:
            if modeType == 'encrpyt':
                num += alphabet.find(key[Index])
            if modeType == 'decrypt':
                num -= alphabet.find(key[Index])
            num %= len(alphabet)
            if symbol.isupper():
                translated.append(alphabet[num])
            elif symbol.islower():
                translated.append(alphabet[num].lower())
            Index += 1
            if Index == len(key):
                Index = 0
        else:
            translated.append(symbol)
    return ''.join(translated)

main()
