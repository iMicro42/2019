#include <stdio.h>

int
main(void)
{
  int counter = 0;
  int number;
  int tempNumber;
  int digitSum = 0;
  int i = 0;
  scanf("%d",&number);

  tempNumber = number;

  while(tempNumber > 0)
  {
    digitSum += (tempNumber%10);
    tempNumber /= 10;
  }


  if(digitSum % 4 == 0)
    printf("%d\n",number);
  else
  {
    tempNumber = number;
    while(i == 0)
    {
      digitSum = 0;
      number+=1;
      tempNumber = number;
      while(tempNumber > 0)
      {
        digitSum += (tempNumber%10);
        tempNumber /= 10;
      }
      if(digitSum % 4 == 0)
        break;

    }
    printf("%d\n",number+counter);
  }

  return 0;
}

/*
End of code!
Date started: 10/19/2019
Date ended: 10/12/2019
Time spent: 20-25 minutes
*/
