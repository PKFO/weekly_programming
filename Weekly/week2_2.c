#include <stdio.h>
int main()
{
   int a[3],Max = 0;
    for(int i = 0 ; i < 3 ; i++){
        scanf("%d",&a[i]);
        if(Max < a[i]);
        Max = a[i];
    }
    printf("%d",Max);
        return 0;
    }
