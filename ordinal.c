/*

* Author: Mohammad Raja

* Course: CSE 1001, Section 02, Fall 2019

* Project: ordinal.c

*/

#include <stdio.h>

int
main(void)
{
  int num; // <-- num is a variable for the user to enter their nunber inside of.
  int sum; // <-- sum is to return the sumn of all the non-negative numbers the user enters.
  sum = 0; // <-- initalizing sum to equal zero.
  printf("Welcome to Ordinal Numbers\n");
  do{
    printf("\nEnter a value between 0 and 65535 (negative value to quit): "); // <-- prompting value from user
    scanf("%d", &num); // <-- getting value from user
    if(num>65535) // <-- if the number is greater then 65535 then tell them input not allowed
      printf("Input not allowed. Try again!\n");
    else if(num>=0 && num<65535) // <-- checks if number is within the limit and if it is it runs through the ordinals -->
    {
      sum+=num; // <-- adds all the values up
      for(int i = 0; i <= num; i++)
      {
        if(i%10 == 1 && i%100 !=11)
          printf("%dst Value\n",i);
        else if(i%10 == 2 && i%100 !=12)
          printf("%dnd Value\n",i);
        else if(i%10 == 3 && i%100 !=13)
          printf("%drd Value\n",i);
        else
          printf("%dth Value\n",i);}
  }
}while(num>=0); // < -- if the number is greater then or equal to zero then keep with the loop if not then go ahead and end it.
  printf("\nThe sum of all your entered numbers is %d",sum);
  printf("\nGoodbye! Thanks for playing.\n\n");
  return 0;
}
