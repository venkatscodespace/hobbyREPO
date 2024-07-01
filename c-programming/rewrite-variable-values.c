#include <stdio.h>
int main() {
    printf("Enter Number: ");
    int n;
    scanf("%d",&n);
    n=n*4; //there is no need to declare the variable again as int 
    printf("%d",n);
}