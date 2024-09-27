#include <stdio.h>
char input(char type[]){
    printf("hello %s \n", type);
}

int main(void){
    char name1[10] = "Frank";
   input(name1);
   char name2[10] = "Doug";
   input(name2);
   char name3[10] = "Larry";
   input(name3);
   char name4[10] = "Chester";
   input(name4);
   char name5[10] = "Gus";
   input(name5);
    return 0;
}