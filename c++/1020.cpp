<<<<<<< HEAD
#include <stdio.h>
 
int main() {

    int time, year, mounth, day;

    scanf("%d", &time);

    year = time / 365;

    mounth = (time - year * 365) / 30;

    day = time - year * 365 - mounth * 30;

    printf("%d ano(s)\n%d mes(es)\n%d dia(s)\n", year, mounth, day);
 
    return 0;
    
=======
#include <stdio.h>
 
int main() {

    int time, year, mounth, day;

    scanf("%d", &time);

    year = time / 365;

    mounth = (time - year * 365) / 30;

    day = time - year * 365 - mounth * 30;

    printf("%d ano(s)\n%d mes(es)\n%d dia(s)\n", year, mounth, day);
 
    return 0;
    
>>>>>>> 1cfb7856b5cd16d06c82bd088e56144c1fd011c8
}