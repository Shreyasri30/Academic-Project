#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int n;
    printf("Enter no. of elements in array: ");
    scanf("%d", &n);
    int a[n];
    printf("Enter array elements: ");
    for(int i=0; i<n; i++)
        scanf("%d", &a[i]);
    for(int i=0;i<n;i++){
        int f=1;
        for(int j=0; j<i; j++){
            if(a[i]==a[j]){
                f=0;
                break;
            }
        }
        if(f==1)
            printf("%d\n", a[i]);
    }
  
    return 0;
}