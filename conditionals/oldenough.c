#include <stdio.h>

int age;

int main(void){
    printf("what is your age?\n");
    scanf("%d", &age);

    if (age >= 18){
        printf("you can vote!\n");
    }else if (age >= 16){
        printf("you can drive!\n");
    } else if (age >=15){
        printf("you can get a learners permit!\n");
    }else {
        printf("you can go to school.");
    }
    return 0;
}