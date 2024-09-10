#include <stdio.h>

int main(void){
   char name[30];
   printf("Please tell me your name: \n");
   fgets(name, sizeof(name), stdin);
   printf("what is a number between 1 and 10: \n");
   fgets(name, sizeof(name), stdin);
    return 0;
}