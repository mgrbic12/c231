alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9",",","."," ",";",":","!"]
ciphertext = ["."," ",";",":","!","M","A","T","H","E","I","C","S","B","D","F","G","J","K","L","N","O","P","Q","R","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9",","]


#1.) Program returns the encrypted and decrypted version of the user input. Allowing you to realize if it follows the scheme presented from pg 34 in the Textbook
message = input("Enter a message to encrypt of decrypt: ").upper()
print()

#encrypt
plaintext_index = []
cipherT = []

for item in message:
    plaintext_index.append(alphabet.index(item))

for piece in plaintext_index:
    cipherT.append(ciphertext[piece])
    
 print("Encrypted Message:")

for token in cipherT:
    print(token, end='')


#decrypt
ciphertext_index = []
plainT = []

for item2 in message:
    ciphertext_index.append(ciphertext.index(item2))

for piece2 in ciphertext_index:
    plainT.append(alphabet[piece2])

print()
print("Decrypted Message:")

for token2 in plainT:
    print(token2, end='')




#encrypted_message = "EO.V7W78.NAE 1GIO.KIB.B R 3C 1.CF.2 3FG .CH .3HE N.FN.CH .O K.BETOIR.EOC RET O3 .B AJE3 ,.CHAFDTHFDC.CH . IARM.IO1.GE11R .V7XUB8.NAE 1GIO.3A IC 1.CH .FATIOEQICEFOIR.NhFDO1ICEFOB.FN.I.3AM0CFRFTE3.BCAD3CDA 8.KHE3H.EOJFRJ 1.EOCF.CH .IAGM.B 3DAECM.IT O3M.EO.KFAR1.KIA.EE,.NAE 1GIO.R 1.CH .CAIOBECEFO.NAFG.0 O3ER.IO1.0I0 A.3AM0CFRFTM.EOCF.CH .GF1 AO. AI8.3HIAI3C AEQ 1.2M.CH .I00RE3ICEFO.FN.GI3HEO B.CF.2FCH.3AM0CFTAI0HM.IO1.3AM0CIOIRMBEB,.H .1E1.CHEB.0AEGIAERM.2M.3F1ENMEOT.KHIC.HI1.IRA I1M.2  O.KAECC O.IO1.2M.I00RMEOT.GICH GICE3B8.0IACE3DRIARM.BCICEBCE3IR.IOIRMBEB8.CF.3AM0CFRFTM,"
#IN 1938, THE JAPANESE REPLACED THE RED MACHINE WITH THE TYPE B MACHINE, WHICH CAME TO BE KNOWN AS PURPLE. IT TOOK A MUCH LARGER TEAM UNDER FRANK ROWLETTS DIRECTION EIGHTEEN MONTHS TO BREAK INTO THIS SYSTEM; THE FIRST TRANSLATION WAS PRODUCED IN SEPTEMBER 1940. IT CAME OUT ONE WEEK AFTER A CRUCIAL KEY TO THE PUZZLE HAD BEEN SUGGESTED BY THE GENEVIEVE GROTJAN, AN SIS JUNIOR CRYPTANALYST. AN ANALOG WAS CONTRUCTED UNDER THE DIRECTION OF THE LE O ROSEN, AN SIS ENGINEER, ANd WHEN IT WAS OPERATIONAL, THE US HAD ACCESS TO ALL OF THE HIGH LEVEL JAPANESE-DIPLOMATIC COMMUNICATIONS. MR. ROWLETT S AWARDS INCLUDE NSA EXCEPTIONAL CIVILIAN SERVICE AWARD, THE NATIONAL INTELLIGENCE DISTINGUISHED SERVICE MEDAL, THE PRESIENTS AWARD FOR DISTINGUISHED FEDERAL CIVILIAN SERVICE, THE NATIONAL SECURITY MEDAL, AND IN 1964 CONGRESS AWARDED HIM 100,00 FOR HIS INVENTIONS HELD SECRETE BY THE GOVERNMENT.

