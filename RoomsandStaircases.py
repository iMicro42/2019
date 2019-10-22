returnList = []

tempList = []

negNumbs = []

x = int(input())

while(x>0):
    x-=1
    counter = 0
    y = int(input())
    z = input()
    y2 = y
    for i in z:
        tempList.append(int(i))

    while(y2>0):
        negNumbs.append(-y2)
        y2-=1

    negNumbs.sort(reverse=True)


    if(tempList.count(0) == y):
        returnList.append(y)
        tempList.clear()
        continue
    elif(tempList[0] == 1 or tempList[-1] == 1):
        returnList.append(y*2)
        tempList.clear()
        continue

    leftIndex = tempList.index(1)
    rightIndex = (len(tempList)) - leftIndex

    for i in negNumbs:
        if tempList[i] == 1:
            if (abs(i) < leftIndex+1):
                rightIndex = abs(i)
                leftIndex  = len(tempList) - rightIndex
                break
    if(rightIndex > leftIndex):
        rightIndex = len(tempList) - leftIndex
        returnList.append(rightIndex*2)
        tempList.clear()
        continue
    elif(leftIndex > rightIndex):
        leftIndex += 1
        returnList.append(leftIndex*2)
        tempList.clear()
        continue
    elif(leftIndex == rightIndex):
        leftIndex = leftIndex+1
        returnList.append(leftIndex*2)
        tempList.clear()
        continue

for i in returnList:
    print(i)

'''
End of code!
Date started: 10/21/2019
Date ended: 10/22/2019
Time spent: 3.5 hours
Codeforce problem: 1244B
'''
