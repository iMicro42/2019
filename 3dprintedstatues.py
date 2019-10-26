n = int(input())
k = n
days = 0;
d3p = 1;

if(n == 1):
    days = 1

else:
    while(n > 0):
        if(d3p < n):
            d3p+=d3p
            days += 1
            continue
        n -= d3p
        days += 1


print(days)


'''
End of code!
Date started: 10/25/2019
Date ended: 10/26/2019
Time spent: 2 hours
Kattis problem: 3d Printed Statues
'''
