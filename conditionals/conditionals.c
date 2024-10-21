#include <stdio.h>

int grade;

int main(void){
    printf("what is your grade percent\n");
    scanf("%d", &grade);

    if (grade >= 90){
        printf("you have an A!\n");
    }else if (grade >= 80){
        printf("you have a B!\n");
    }else if (grade >= 70){
        printf("you have a C.\n");
     }else if (grade >= 60){
        printf("you have a D :(\n");
    } else{
        printf("you have an F! :'(\n");
        }
    return 0;
}