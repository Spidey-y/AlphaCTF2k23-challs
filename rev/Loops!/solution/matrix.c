#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main(int argc, char const *argv[])
{

  FILE *ptr;
  char *buffer ;
  int nrows, ncolumns, cres, rres,length,len;
  ptr = fopen("flag.txt", "r");

  if (NULL == ptr)
  {
    printf("file can't be opened \n");
    exit(0);
  }
  fseek(ptr, 0, SEEK_END);
  length = ftell(ptr);
  fseek(ptr, 0, SEEK_SET);
  buffer = malloc(length);
  if (buffer)
  {
    fread(buffer, 1, length, ptr);
  }else
  {
    printf("malloc error");
    exit(1);
  }
  fclose(ptr);
  nrows = sqrt(length) ;
  ncolumns = sqrt(length);
  
  int *array3 = malloc(nrows * ncolumns * sizeof(int));
  int *array = malloc(ncolumns * sizeof(int));
  int *array2 = malloc(nrows * sizeof(int));
  int *array4 = malloc((ncolumns + nrows * ncolumns) * sizeof(int));

  for (int i = 0; i < ncolumns; i++)
  {
    for (int j = 0; j < nrows; j++)
    {
      array3[i * ncolumns + j] = buffer[i * ncolumns + j];
    }
  }
  for (int j = 0; j < nrows; j++)
  {
    cres = 0;
    for (int i = 0; i < ncolumns; i++)
    {
      cres += (int)array3[i * ncolumns + j];
    }
    array[j] = cres;
  }

  for (int j = 0; j < ncolumns; j++)
  {
    rres = 0;
    for (int i = 0; i < nrows; i++)
    {
      rres += (int)array3[j * ncolumns + i];
    }
    array2[j] = rres;
    array4[j] = array2[j];
  }

  int out = 0;
  for (int i = 0; i < ncolumns; i++)
  {
    for (int j = 0; j < nrows; j++)
    {
      out = array2[i] + array[j];
      out = out ^ (int)array3[i * ncolumns + j];
      array4[ncolumns * j + ncolumns + i] = out;
    }
  }
  for (int i = 0; i < ncolumns * nrows + ncolumns; i++)
  {
    printf("%d ", array4[i]);
  }
  
  free(array3);
  free(array);
  free(array4);
  free(array2);

  return 0;
}
