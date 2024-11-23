#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int size, i, position, element;
    printf("Enter size of array: ");
    scanf("%d", &size);
    int array[size + 1];
    printf("Enter elements of array: ");
    for (i = 0; i < size; i++){
        scanf("%d", &array[i]);
    }
    printf("Enter position where element is to be inserted: ");
    scanf("%d", &position);
    printf("Enter element to be inserted: ");
    scanf("%d", &element);
    if (position > size){
        printf("Invalid Input\n");
    } 
    else {
        for (i = size; i >= position; i--){
            array[i] = array[i - 1];
        }
        array[position - 1] = element;
        printf("Array after insertion is\n");
        for (i = 0; i <= size; i++){
            printf("%d\n", array[i]);
        }
    }

    return 0;
}
