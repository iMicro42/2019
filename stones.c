#include <stdio.h>

int
main(void)
{
  int length;

  scanf("%d", &length);

  int counter=0,temp=0;

  int a[length];  int b[length];   int c[length];

  int *p = a;     int *p2 = b;     int *p3 = c;

  for(int i = 0; i<length; i++)
  {

    scanf("%d %d %d",p,p2,p3);
    p++;
    p2++;
    p3++;

  }

  for(int i = 0; i<length; i++)
  {
    counter = 0;
    if(b[i]>0)
    {
      if(b[i] > c[i])
        {
          while(c[i]>=2 && b[i]>0)
          {
            temp = c[i] -2;

            counter +=2;

            c[i] = temp;

            temp = b[i] -1;

            counter +=1;

            b[i] = temp;
          }

          while(b[i] >= 2 && a[i] > 0)
            {
              temp = b[i] -2;

              counter += 2;

              b[i] = temp;

              temp = a[i] -1;

              counter+= 1;

              a[i] = temp;
            }

        }
      else if(c[i] >= b[i] && c[i] > 1)
          {
            while(c[i] >= 2 && b[i] > 0)
              {
                temp = c[i] -2;

                counter += 2;

                c[i] = temp;

                temp = b[i] -1;

                counter+= 1;

                b[i] = temp;
              }
            while(b[i]>=2 && a[i]>0)
              {
                temp = b[i] -2;

                counter +=2;

                b[i] = temp;

                temp = a[i] -1;

                counter +=1;

                a[i] = temp;
              }
          }
        printf("%d\n",counter);
    }
    else
      printf("0\n");

  }

}


/*
End of code!
Date started: 10/19/20
Date ended: 10/19/20
Time spent: 35 minutes
*/
