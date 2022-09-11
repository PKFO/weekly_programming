#include <stdio.h>
#include <string.h>
int main()
{
    int n, k = 0;
    char str[100];
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            str[k] = '*';
            k++;
        }
        str[k] = '\n';
        k++;
    }
    for (int i = 0; i < strlen(str); i++)
    {
        printf("%c", str[i]);
    }

    return 0;
}