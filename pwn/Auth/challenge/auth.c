#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ARRAY_SIZE 100000

const static char *secret = "Alph@bit_club";

int main(int argc, char **argv)
{
    char *buf = malloc(ARRAY_SIZE);
    printf("buffer at: %p\n", buf);
    printf("Y0ur p4$$w0rd: ");
    fflush(stdout);
    fgets(buf, ARRAY_SIZE, stdin);

    if (strstr(secret, buf))
    {
        printf("How did you get that !!!!\n");
        exit(-1);
    }

    if (strstr(buf, secret))
    {
        printf("welcome, H4ck3r\n");
        FILE *File = fopen("flag.txt", "r");
        if (File == NULL)
        {
            fprintf(stderr, "[x] flag.txt file does not exist\n");
            exit(-1);
        }
        fgets(buf, ARRAY_SIZE, File);
        printf("here's your flag... %s\n", buf);
    }
    else
    {
        printf("nice right :)\n");
    }

    free(buf);
}