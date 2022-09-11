#include <stdio.h>
int main(){
    int a,b,c;
    scanf("%d %d %d",&a,&b,&c);
    if(a + b >= a + c && a + b >= b +c){
        printf("%d",a +b);
    }
    else if(b + c >= a+c && b + c >= b+a){
        printf("%d", b+c);
    }
    else if(c + a >= b+a && c + a >= c+b){
        printf("%d",c +a);
    }
}