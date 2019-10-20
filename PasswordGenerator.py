import random
chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()?><:|{}+_~-=[].,/';'"

passwordOut = []

for x in range(20):
    y = random.randint(0,65)
    passwordOut.append(chars[y])

x = ''.join(passwordOut)

print(x)

