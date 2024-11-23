#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int frnds, teams;
    int n1, n2;

    printf("Enter no.of friends:\n");
    scanf("%d", &frnds);
    printf("Enter no.of teams:\n");
    scanf("%d", &teams);

    n1 = frnds / teams;
    n2 = frnds % teams;

    printf("The number of friends in each team is %d and left out is %d\n", n1, n2);

    return 0;
}
