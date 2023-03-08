#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *bin_to_ascii(char *bin)
{
    size_t bin_len = strlen(bin);
    char *result = malloc((bin_len / 8) + 1);
    for (size_t i = 0; i < bin_len; i += 8)
    {
        int decimal = 0;
        for (int j = 0; j < 8; j++)
        {
            decimal *= 2;
            decimal += bin[i + j] - '0';
        }
        result[i / 8] = (char)decimal;
    }
    result[bin_len / 8] = '\0';
    return result;
}

int main(int argc, char const *argv[])
{
    char *character;
    char *buf;
    int i;
    int s[8];
    int len, ncolumns;
    ncolumns = 8;
    len = strlen(argv[1]);
    if ((argc != 2))
    {
        printf("Usage %s <string> ", argv[0]);
        exit(1);
    }
    if ((len != 24))
    {
        puts("Not the right length!!");
        exit(1);
    }
    buf = argv[1];
    int a, b;
    for (int k = 0; k < 3; k++)
    {
        int *array3 = malloc(8 * 8 * sizeof(int));
        for (int j = 0; j < 8; j++)
        {
            character = (buf + j + (k * 8));
            for (i = 0; i < 8; i++)
            {
                s[i] = *character % 2;
                *character = *character / 2;
            }
            for (b = 0, a = 7; b < 8; b++, a--)
            {
                array3[b * ncolumns + j] = s[a];
            }
        }
        char tmp[64];
        for (int i = 0; i < 64; i++)
        {
            sprintf(tmp + i, "%d", array3[i]);
        }
        free(array3);
        tmp[64] = '\0';
        char *ascii = bin_to_ascii(tmp);
        for (int i = 0; i < 8; i++)
        {
            printf("%c", ascii[i]);
        }
        free(ascii);
    }

    return 0;
}
