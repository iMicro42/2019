/*

Equal Prices

*/

#include <stdio.h>

int
main(void)
{
  int length;
  scanf("%d",&length);
  int returnArr[length];
  for(int i = 0; i<length; i++)
  {
    int length2;
    scanf("%d",&length2);
    int array[length2];
    int sum=0;
    for(int j = 0; j<length2;j++)
    {
      scanf("%d",&array[j]);
      sum+=array[j];
    }
    for (int k = 0; k < length2; k++)
    {
      for (int j = 0; j < length2; j++)
      {
        if (array[j] > array[k])
        {
          int tmp = array[k];
          array[k] = array[j];
          array[j] = tmp;
        }
      }
    }
    for(int j = 1; j<=sum; j++)
    {
      if((j*length2)>=sum)
      {
        returnArr[i] = j;
        break;
      }
    }
  }
  for(int i = 0; i<length; i++)
  {
    printf("%d\n",returnArr[i]);
  }
return 0;
}

/*
End of code
Date started: 10/24/2019
Date ended: 10/25/2019
Time spent: 1.5 hours
Codeforces problem: 1234A
*/
