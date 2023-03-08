#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 100
#include <string.h>
int main()
{
    char a[MAX];
    fprintf(stdout, "Let me check your secret: ");
    fgets(a, MAX, stdin);
    fprintf(stdout, "Hmmm, that seems wrong");    
    int fl4g[] = {196, 233, 245, 237, 228, 198, 209, 195, 254, 161, 192, 224, 218, 247, 224, 243, 192, 215, 214, 182, 218, 180, 214, 218, 182, 196, 161, 220, 248};
    char fl44444g[] = "";
    int hehe = 0x85; 
    for (int x = 0; x < 29; x++) {
        char ch = fl4g[x] ^ hehe;
        strncat(fl44444g, &ch, 1);
    } 
    return 0;
    
}