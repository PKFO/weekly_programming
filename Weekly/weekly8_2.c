#include <stdio.h>
int main()
{
      int n;
      scanf("%d", &n);
      int center = n;
      for (int i = 1; i <= n; i++)
      {
            for (int j = 1; j <= (n*2)-1; j++)
            {
                 if(i == 1 && j == n){
                  printf("*");
                 }
                 else if(j > center - i && j < center + i){
                  printf("*");
                 }
                 else{
                  printf(" ");
                 }
            }
            printf("\n");
      }
      return 0;
}