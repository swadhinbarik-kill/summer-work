#include <stdio.h>
#include <ctype.h>
int main(void)
{

    int n,*p;
    //scanf("%d",&n);
    int a[3]={1,2,3};
    p =&a;
    //for(int i=0;i<3;i++){
      //  scanf("%d",&a[i]);
    //}-2061502460

    //printf("%d",p);
    printf("\n");
    for(int i=0;i<3;i++){
    printf("%d\n",*(p+i));
    printf("%d\n",&*(p+i));

    }


}























