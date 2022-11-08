#include <stdio.h>
int main(){
    FILE *fp;
    char x[100];
    printf("input data string: ");
    fp = fopen("data2.txt","w");
    for(int i = 0;i<100;i++){
        scanf("%c",&x[i]);
        if(x[i] != '.'){
            fprintf(fp,"%c",x[i]);
        }
        else{
            fprintf(fp,".");
            break;
        }
    }
    fclose(fp);
    return 0;
}