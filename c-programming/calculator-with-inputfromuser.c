#include <stdio.h>
int main(void)
{
    printf("Number 1:");
    int n1;
    scanf("%d",&n1);
    printf("Number 2:");
    int n2;
    scanf("%d",&n2);
    printf("%d is the sum of number 1 and 2.\n %d is the difference between number 1 and 2. \n %d is the product of number 1 and 2. \n %d is the quotient of number 1 and 2. \n",n1+n2,n1-n2,n1*n2,n1/n2);
}