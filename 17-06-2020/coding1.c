// C program to replace all 0’s with 1 in a given integer
#include  
int replace (long int num)
{
     // Base case for recursion termination
     if (num == 0)
        return 0;
     // Extract the last digit and change it if needed
     int digit = num % 10;
     if (digit == 0)
         digit = 1;
     // Convert remaining digits and append the last digit

     return replace(num/10) * 10 + digit;
}
int Convert(long int num)
{
     if (num == 0)
        return 1;
     else
       return replace(num);
}
int main()
{
      long int num;
     //To take user input
      printf("\nInsert the num : ");
      scanf("%d", &number);
      //display final result
      printf("\n Num after replacement : %d\n", Convert (num));
      return 0;
