alphabetDict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

print("\n***This program decrypts your sentence that was encrypted by a ceaser cipher***\n")

plainText = raw_input("Enter the sentence you want decrypted> ")

keyRL = raw_input("\nWhat way was your sentence encrypted?> ")

key = raw_input("\nEnter the number of letters your sentence was shifted shifted?> ")

keyRL = keyRL.lower()

plainText = plainText.lower()

tempEncryptedSentence = []

for letter in plainText:
    if letter == ' ':
        tempEncryptedSentence.append(letter)
    for letters,num in alphabetDict.items():
        if letters == letter:
            if keyRL == 'right':
                tempForm = (int(num) - int(key)) % 26
                for letters2,num2 in alphabetDict.items():
                    if num2 == tempForm:
                        tempEncryptedSentence.append(letters2)
            elif keyRL == 'left':
                    tempForm = (int(num) + int(key)) % 26
                    for letters2,num2 in alphabetDict.items():
                        if num2 == tempForm:
                            tempEncryptedSentence.append(letters2)

encryptedSentence = ''.join(tempEncryptedSentence)

if keyRL == "right":
    keyRL = "left"
elif keyRL == 'left':
    keyRL = 'right'

print("Your sentence has been decrypted by being shifted {} units to the {} > ".format(key,keyRL) + encryptedSentence)

