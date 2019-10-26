#include <stdio.h>

int
main(void)
{
  int a,b,c;
  int returnNum[3];
  scanf("%d %d %d",&a,&b,&c);
  char order;

  if(a>b)
  {
    int temp = a;
    a = b;
    b = temp;
  }
  if(b>c)
  {
    int temp = c;
    c = b;
    b = temp;
  }
  if(a>b)
  {
    int temp = a;
    a = b;
    b = temp;
  }
  for(int i = 0; i<3; i++)
  {
    scanf(" %c",&order);
    if(order == 'A')
      returnNum[i]=a;
    else if(order == 'B')
      returnNum[i]=b;
    else if(order == 'C')
      returnNum[i]=c;
  }
  for(int i = 0; i<3; i++)
  {
    printf("%d ",returnNum[i]);
  }
  printf("\n");
}


/*
END OF CODE!
Date started: 10/26/2019
Date ended: 10/26/2019
Time spent: 25 minutes
Kattis problem: ABC
*/
