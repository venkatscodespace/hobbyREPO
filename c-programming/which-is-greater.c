#include <stdio.h>
int main() {
    printf("Enter Number 1: ");
    int n1;
    scanf("%i",&n1);
    printf("Enter Number 2: ");
    int n2;
    scanf("%i",&n2);
    if (n1>n2){
        printf("%d is greater than %d.\n",n1,n2);
    }
    else if (n1<n2){
        printf("%d is greater than %d.\n",n2,n1);
    }
    else {
        printf("Both numbers are equal.\n");
    return 0;
    }
}
