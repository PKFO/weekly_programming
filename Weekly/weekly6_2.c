#include<stdio.h>
int main(){
    printf("data in array:");
    int a[10];
    scanf("%d %d %d %d %d %d %d %d %d %d",&a[0],&a[1],&a[2],&a[3],&a[4],&a[5],&a[6],&a[7],&a[8],&a[9]);
    if(a[0]%2 != 0 && a[2]%2 != 0){
        printf("%d",a[1]);
    }
    if(a[1]%2 != 0 && a[3]%2 != 0){
        printf("%d ",a[2]);
    }
if(a[2]%2 != 0 && a[4]%2 != 0){
        printf("%d ",a[3]);
    }
if(a[3]%2 != 0 && a[5]%2 != 0){
        printf("%d ",a[4]);
    }
    if(a[4]%2 != 0 && a[6]%2 != 0){
        printf("%d ",a[5]);
    }
if(a[5]%2 != 0 && a[7]%2 != 0){
        printf("%d ",a[6]);
    }
if(a[6]%2 != 0 && a[8]%2 != 0){
        printf("%d ",a[7]);
    }
if(a[7]%2 != 0 && a[9]%2 != 0){
        printf("%d ",a[8]);
    }
    return 0;
}