#include <stdio.h>

int
main(void)
{
  int cases;
  int num;

  scanf("%d",&cases);
  double returnN[cases];
  for(int i = 0; i<cases; i++)
  {
    scanf("%d",&num);
    double numbers[num];
    double counterN = 0;
    double average = 0;
    for(int j = 0; j<num; j++)
    {
      scanf("%lf",&numbers[j]);
      counterN += numbers[j];
      if(j == num-1)
      {
        average = counterN / num;
      }
    }
    double counter = 0;
    for(int j = 0; j<num; j++)
    {
      if(numbers[j]>average)
      {
        counter+=1;
      }
      if(j == num-1)
      {
        counter = counter/num * 100;
        returnN[i]=counter;
        break;
      }
    }
  }

for(int i = 0; i<cases; i++)
{
  printf("%.3lf%%\n",returnN[i]);
}

}
/*
End of code!
Date started: 10/25/2019
Date ended: 10/25/2019
Time spent: 35 minutes
Kattis problem: Above average problem
*/
