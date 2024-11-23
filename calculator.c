#include<stdio.h>
int main()
{
	float a,b;
    int choice;
	printf("Enter two numbers a and b:");
	scanf("%f%f",&a,&b);
	printf("\n Enter 1 for addition");
	printf("\n Enter 2 for subtraction");
	printf("\n Enter 3 for multiplication");
	printf("\n Enter 4 for division");
	printf("\n Enter your choice:");
    scanf("%d",&choice);
	
	switch(choice)
	{
		case 1:
			printf("Sum is: %f",a+b);
			break;
		case 2:
			printf("Difference is: %f",a-b);
			break;
		case 3:
			printf("Product is: %.2f",a*b);
			break;	
		case 4:
			printf("Division is: %.2f",a/b);
			break;
	default:	
	printf("Invalid choice:");
	}	
}