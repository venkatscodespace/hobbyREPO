#include <stdio.h>
int main() {
    printf("Enter Number: ");
    int n;
    scanf("%d",&n);
    printf("Before Updation of value: %d",n);
    n=n*4; //there is no need to declare the variable again as int 
    printf("After Updation of value: %d",n);
}