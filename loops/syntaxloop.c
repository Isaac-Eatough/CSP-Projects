#include <stdio.h>
char siblings[8][20] = {"Zach","Kaden","Alex","Lucah","Isaac"};
int i;
int main (){
   while (i < 5){
    printf("%s Eatough\n", siblings[i]);
    i+=1;
   }
    return 0;
}