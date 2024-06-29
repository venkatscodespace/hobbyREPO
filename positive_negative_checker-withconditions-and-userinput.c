#include <stdio.h>
int main(void)
{
    printf("Enter a number: ");
    int n;
    scanf("%d",&n);
    if (n>0){
        printf("%d is greater than 0, and is a positive number.",n);
    }
    else if (n<0){
        printf("%d is lesser than 0, and is a negative number.",n);
    }
    else {
        printf("%d is neither positive nor negative.");
    }
}
