#include <stdio.h>
int main(){
    float a[10],sum = 0;
    for(int i = 0;i <10;i++){
        printf("Height %d :",i+1);
        scanf("%f",&a[i]);
        sum += a[i];
    }
    for(int i = 0;i<10;i++){
        printf("Height %d : %f\n",i+1,a[i]);
    }
    printf("average of height:%.2f",sum/10);
    return 0;
}