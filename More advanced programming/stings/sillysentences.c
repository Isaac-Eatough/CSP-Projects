#include <stdio.h>
#include <string.h>

int main(void){
    char name[20], place[20], verb[20], noun[20], sentence[500];
    printf("Type a name: ");
    fgets(name, sizeof(name), stdin);
    printf("Type a place: ");
    fgets(place, sizeof(place), stdin);
     printf("Type a verb: ");
   fgets(verb, sizeof(verb), stdin);
     printf("Type a noun: ");
     fgets(noun, sizeof(noun), stdin);
    strcat(sentence, name);
    strcat(sentence, " went to the ");
    strcat(sentence, place);
    strcat(sentence, " where they ");
    strcat(sentence, verb);
    strcat(sentence, " and bought a ");
    printf("%s", sentence);
   // printf("%s went to the %s where he %s,and bought a %s.", name, place, verb, noun);
    return 0;
}