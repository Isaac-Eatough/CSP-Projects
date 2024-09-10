#include <stdio.h>

int main(void){
   char name[50];
   printf("enter your name: ");
   fgets(name, sizeof(name), stdin);
   printf("hello, %s! Welcome to the program.\n, name");
    return 0;
}