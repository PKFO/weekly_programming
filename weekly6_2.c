#include <stdio.h>
int main()
{
    int a[3], max = 0, max1;
    for (int i = 0; i < 3; i++)
    {
        scanf("%d", &a[i]);
        if (max < a[i])
        max = a[i];
    }
    if (a[0] >= a[1] && a[0] <= a[2])
    {
        max1 = a[0];
    }
    else if (a[0] <= a[1] && a[0] >= a[2])
    {
        max1 = a[0];
    }
    else if (a[1] >= a[0] && a[1] <= a[2])
    {
        max1 = a[1];
    }
    else if (a[1] <= a[0] && a[1] >= a[2])
    {
        max1 = a[1];
    }
    else if (a[2] >= a[0] && a[2] >= a[1])
    {
        max1 = a[2];
    }
    else if (a[2] <= a[1] && a[2] >= a[0])
    {
        max1 = a[2];
    }
    printf("%d", max + max1);
    return 0;
}