#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int n1,n2;
    printf("Enter value of number of elements in array 1: ");
    scanf("%d", &n1);
    int a1[n1];
    for(int i = 0; i<n1; i++){
        printf("Enter array elements of array 1: ");
        scanf("%d", &a1[i]);
    }
    printf("Enter value of number of elements in array 2: ");
    scanf("%d", &n2);
    int a2[n2];
    for(int i = 0; i<n2; i++){
        printf("Enter array elements of array 2: ");
        scanf("%d", &a2[i]);
}
    if (n1 != n2){
        printf("Incompatible\n");
        return 0;
    }
    for(int i = 0; i<n1; i++){
        if(a1[i] < a2[i]){
            printf("Incompatible\n");
            return 0;
        }
    }
    printf("Compatible\n");
    return 0;
  
   
}
