#include <stdio.h>

int
main(void)
{
int length,num,returnCounter = 0,counter = 0,cCounter = 0;

scanf("%d",&length);

int numbers[length];

int checker[length];

for(int i = 0;i<length; i++)
{
  checker[i] = 0;
}

for(int i = 0; i<length;i++)
{
  scanf("%d",&num);
  numbers[i] = num;
}

for (int i = 0; i < length; i++)
{
	for (int j = 0; j < length; j++)
	{
		if (numbers[j] > numbers[i])
		{
			int tmp = numbers[i];
			numbers[i] = numbers[j];
			numbers[j] = tmp;
		}
	}
}

for(int i = 0; i<length;i++)
{
  for(int j = 0; j<length; j++)
  {
    if(numbers[j] == 0) continue;
    if(numbers[j] % numbers[i]== 0)
    {
      counter = 0;
      for(int k = 0; k<length; k++)
      {
        if (checker[k] == 0) continue;
        if(numbers[j]%checker[k] == 0)
        {
          counter = 1;
          break;
        }
      }
      if (counter == 1) break;
      returnCounter +=1;
      checker[cCounter] = numbers[i];
      cCounter+=1;
      break;
    }
    else if(j == length-1)
    {
      returnCounter+=1;

    }
  }
}

printf("%d\n",returnCounter);

return 0;
}

/*
End of code!
Date started: 10/12/2019
Date ended: 10/19/2019
Time spent: 15 hours
*/
