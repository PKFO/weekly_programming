#include <stdio.h>
#include <string.h>
int main()
{
    FILE *fp;
    char x[100];
    int i = 0;
    fp = fopen("data.txt", "w");
    printf("input string :");
    do
    {
        scanf("%c", &x[i]);
        fprintf(fp, "%c", x[i]);
    } while (x[i] != '.');
    fclose(fp);
    return 0;
}