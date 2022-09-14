#include <stdio.h>
int main(){
    printf("data in array:");
    int a[10];
    scanf("%d %d %d %d %d %d %d %d %d %d",&a[0],&a[1],&a[2],&a[3],&a[4],&a[5],&a[6],&a[7],&a[8],&a[9]);
    printf("Result:");
    for(int i = 0;i<10;i++){
        if(a[i-1]%2 != 0){
        if(a[i+1] % 2 != 0){
            printf("%d ",a[i]);
        }
        }
    }
    





    return 0;
}