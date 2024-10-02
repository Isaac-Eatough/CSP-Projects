#include <stdio.h>
#include <time.h>

int hour;


int main(void){
    time_t now;
   struct tm*now_tm;

   now = time(NULL);
   now_tm = localtime(&now);
   hour = now_tm->tm_hour;
   printf("%d\n", hour);

   if (hour <= 12){
    printf("good Morning!\n");
   }else if (hour <= 18){
    printf("good Afternoon!\n");
   }else if (hour <= 20){
    printf("good Evening!\n");
   }else{
    printf("good Night!\n Go to sleep NOW!!!!");
   }

    return 0;
}