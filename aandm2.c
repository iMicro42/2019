#include <stdio.h>

int
main(void)
{
int num;
int length;
int change;

scanf("%d %d",&length,&change);
int numbers[length];
int returnNumbers[length];

for (int i = 0; i < length; i++) {
    scanf("%1d", &numbers[i]);
}
if(change == 1 && length==1)
  returnNumbers[0] = 0;

else{
int counter = 0;
for(int i =0; i<length; i++)
{
  int j = numbers[i];
  if(change>0)
  {
    if(j==0)
    {
      returnNumbers[i] = 0;
      continue;
    }
    else if(i==0 && j==1)
    {
      returnNumbers[i] = 1;
      continue;
    }
    change-=1;
    if(j>1 && i==0)
    {
      returnNumbers[i]=1;
      continue;
    }
    else if(j>0)
    {
      returnNumbers[i]=0;
      continue;
    }
  }
  else
    returnNumbers[i] = j;
}
}

for(int i = 0; i<length; i++)
  printf("%d",returnNumbers[i]);

printf("\n");
return 0;
}

/*
End of code!
Date started: 10/22/2019
Date ended: 10/24/2019
Time spent: 3.5 hours
Codeforces problem: #1230
*/
