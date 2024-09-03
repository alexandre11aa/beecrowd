<<<<<<< HEAD
#include <stdio.h>
 
int main() {

    int time, hour, minute, second;

    scanf("%d", &time);

    hour = time / 3600;

    minute = (time - hour * 3600) / 60;

    second = time - hour * 3600 - minute * 60;

    printf("%d:%d:%d\n", hour, minute, second);
 
    return 0;
    
=======
#include <stdio.h>
 
int main() {

    int time, hour, minute, second;

    scanf("%d", &time);

    hour = time / 3600;

    minute = (time - hour * 3600) / 60;

    second = time - hour * 3600 - minute * 60;

    printf("%d:%d:%d\n", hour, minute, second);
 
    return 0;
    
>>>>>>> 1cfb7856b5cd16d06c82bd088e56144c1fd011c8
}