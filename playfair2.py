'''

Encrypts files using a playfair cipher 6x6

'''


# Creating a variable for the alphanumeric square that will be used -- >
alphabetSquare = {}

# Getting file name to read from and file name to write encrypted text to -- >
print("Enter your file name: ")
fileName = input()

print("Enter encrypted file name: ")
encryptedFile = input()

# Opening file to read from and creating file to write encrypted text to -- >
fRead = open(fileName, 'r')

fWrite = open(encryptedFile,'w')

fRead2 = fRead.read().lower()


# Getting key from user -- >
print("Enter your alphanumeric key: ")
key = input()

# Going over key and adding to start of alphabetSquare & making alhpabetSquare-- >

counter = 1
for letter in key:
    if letter not in alphabetSquare:
        if letter == " " or letter == "\n":
            continue
        if letter in "[@_!#$%^&*()<>?/|}{~:].,''``":
            continue
        letter = letter.lower()
        alphabetSquare[letter] = counter
        counter+=1
        if letter == key[-1]:
            for let in "abcdefghijklmnopqrstuvwxyz0123456789":
                if counter <= 36:
                    if let in alphabetSquare:
                        continue
                    else:
                        alphabetSquare[let] = counter
                        counter += 1


# going over every letter in file and appending it to a list to be used later -- >
fileLetters = []

for letter in fRead2:
    if letter == " " or letter == "\n":
        continue
    if letter in "[@_!#$%^&*()<>?/|}{~:].,''``":
        continue
    fileLetters.append(letter)

if len(fileLetters) % 2 != 0:
    fileLetters.append('z')

# loops through fileLetters and assigns a number to each character

numberCharList = []

for char in fileLetters:
    for letters,num in alphabetSquare.items():
        if char == letters:
            numberCharList.append(num)

print(numberCharList)
print(alphabetSquare)
#rows to loop through
row1 = [1,2,  3,4,    5,6]
row2 = [7,8,  9,10, 11,12]
row3 = [13,14,15,16,17,18]
row4 = [19,20,21,22,23,24]
row5 = [25,26,27,28,29,30]
row6 = [31,32,33,34,35,36]

row = [row1,row2,row3,row4,row5,row6]

#columns to loop through
column1 = [1,7,13,19,25,31]
column2 = [2,8,14,20,26,32]
column3 = [3,9,15,21,27,33]
column4 = [4,10,16,22,28,34]
column5 = [5,11,17,23,29,35]
column6 = [6,12,18,24,30,36]

column = [column1, column2, column3, column4, column5, column6]

# loops through numCharList and checks wheter the characters in same row/column or different row and column and uses cipher
temp = []
encryptedLetters = []
for number in numberCharList:
    temp.append(number)
    counter = 0
    print(temp)
    if len(temp) == 2:
        for x in range(1):
            for rows in row:
                if temp[0] in rows and temp[1] in rows:
                    for n in range(2):
                        for i in range(1,7):
                            if temp[n] == 6 * i:
                                if i == 1:
                                    right = 1
                                else:
                                    right = 1 + (6*i)
                                for letter,num in alphabetSquare.items():
                                    if right == num:
                                        encryptedLetters.append(letter)
                                        counter+=1
                                        break
                            elif counter == n and temp[n] % 6 != 0:
                                right = temp[n] + 1
                                for letter,num in alphabetSquare.items():
                                    if right == num:
                                        encryptedLetters.append(letter)
                                        counter += 1
                                        break

            if counter > 0:
                temp.clear()
                break
            if counter == 0:
                for columns in column:
                    if temp[0] in columns and temp[1] in columns:
                        for n in range(2):
                            for i in range(1,7):
                                if temp[n] == 30 + i:
                                    for letter,num in alphabetSquare.items():
                                        if i == num:
                                            encryptedLetters.append(letter)
                                            counter+=1
                                elif counter == n:
                                    down = temp[n] + 6
                                    for letter,num in alphabetSquare.items():
                                        if  down == num:
                                            encryptedLetters.append(letter)
                                            counter+=1
            if counter > 0:
                temp.clear()
                break
            if counter == 0:
                for rows in row:
                    for nums in rows:
                        if temp[0] == nums:
                            indexX = rows.index(nums)
                            numrowX = rows
                        if temp[1] == nums:
                            indexY = rows.index(nums)
                            numrowY = rows
                for rows in row:
                    for nums in rows:
                        if(rows == numrowX and rows.index(nums) == indexY):
                            for letter,num in alphabetSquare.items():
                                if nums == num:
                                    encryptedLetters.append(letter)
                for rows in row:
                    for nums in rows:
                        if(rows == numrowY and rows.index(nums) == indexX):
                            for letter,num in alphabetSquare.items():
                                if nums == num:
                                    encryptedLetters.append(letter)

                temp.clear()
            if counter > 0:
                temp.clear()
                break


# writes the pairs to the file.
temp2 = []
for letters in encryptedLetters:
    temp2.append(letters)
    if len(temp2) == 2:
        temp3 = ''.join(temp2)
        fWrite.write(temp3)
        fWrite.write(' ')
        temp2.clear()


fWrite.close()
fRead.close()

'''
End of code!
start date: 9/29/2019
end date: 10/11/2019
Time spent: 16 hours
'''
