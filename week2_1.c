#include <stdio.h>

int main()
{
    int a, b, c;
    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%d", &c);
    if (a > b && b > c)
    {
        printf("%d", a);
        }
        else if (a > c && c > b)
        {
            printf("%d", a);
        }
        else if (b > a && a > c)
        {
            printf("%d", b);
        }
        else if (b > c && c > a)
        {
            printf("%d", b);
        }
        else if (c > a && a > b)
        {
            printf("%d", c);
        }
        else if (c > b && b > a)
        {
            printf("%d", c);
        }
        else if (a == b == c)
        {
            printf("%d", a);
        }

    return 0;
}