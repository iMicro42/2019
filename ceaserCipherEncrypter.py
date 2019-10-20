alphabetDict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

print("\n***This program encrypts your sentence using a ceaser cipher***\n")

plainText = raw_input("Enter the sentence you want encrypted> ") # <-- gets plainText

keyRL = raw_input("\nWhat way do you want your letters shifted right or left?> ") # <-- gets one half of the key for what way of the alphabet this cipher moves

key = raw_input("\nEnter the number of letters you want shifted?> ") # <-- gets second half of key for how many numbers right or left

keyRL = keyRL.lower()

plainText = plainText.lower()

tempEncryptedSentence = [] # <-- making a list to append encrypted letters to

for letter in plainText: # <-- loops through every letter in the plainText
    if letter == ' ': # <-- if their is an empty space it will append that to tempEncryptedSentence
        tempEncryptedSentence.append(letter)
    for letters,num in alphabetDict.items(): # <-- loops through the alphabet to find which letter and number the letter in plainText loop correalates to.
        if letters == letter:
            if keyRL == 'right': # <-- if the first half of the key is right this loop will start
                tempForm = (int(num) + int(key)) % 26 # <-- finds the number shifted right after making sure the number stays under 26 equal to how many alphabet letters their are
                for letters2,num2 in alphabetDict.items(): # <-- loops through alphabet again to find the letter that the Encrypted number correlates to, in order to add encrypted letter into tempEncryptedSentence
                    if num2 == tempForm: # <-- checks if current value of letter in loop is equal to the encrypted number, if it is then -- >
                        tempEncryptedSentence.append(letters2)# <-- adds encrypted Letter to list tempEncryptedSentence
            elif keyRL == 'left':
                    tempForm = (int(num) - int(key)) % 26
                    for letters2,num2 in alphabetDict.items():
                        if num2 == tempForm:
                            tempEncryptedSentence.append(letters2)

encryptedSentence = ''.join(tempEncryptedSentence) # <-- joins the encrypted sentence back into the form it was passed in
print("Your encrypted sentence has been shifted {} units to the {} > ".format(key,keyRL) + encryptedSentence)

