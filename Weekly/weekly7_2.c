#include <stdio.h>
int main(){
    float a[10],sum = 0;
    scanf("%f %f %f %f %f %f %f %f %f %f",&a[0],&a[1],&a[2],&a[3],&a[4],&a[5],&a[6],&a[7],&a[8],&a[9]);
    sum = a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]+a[9];
    printf("Height 1: %f\n",a[0]);
    printf("Height 2: %f\n",a[1]);
    printf("Height 3: %f\n",a[2]);
    printf("Height 4: %f\n",a[3]);
    printf("Height 5: %f\n",a[4]);
    printf("Height 6: %f\n",a[5]);
    printf("Height 7: %f\n",a[6]);
    printf("Height 8: %f\n",a[7]);
    printf("Height 9: %f\n",a[8]);
    printf("Height 10: %f\n",a[9]);
    printf("average of height : %0.2f\n",&sum);
    return 0 ;
}