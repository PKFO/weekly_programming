#include <stdio.h>
int main()
{
    int x, b = 1;
    scanf("%d", &x);
    for (int i = 1; i <= x; i++)
    {
        for (int s = 0; s <= x - i; s++)
        {
            printf(" ");
        }
        for (int j = 0; j < (i * 2) - 1; j++)
        {
            printf("*");
        }
        printf("\n");
        b++;
    }

    return 0;
}
