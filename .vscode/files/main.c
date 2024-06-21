#include <stdio.h>
#include <stdlib.h>

int main()
{
    int arr[]={2,5,6,1};
    int temp;
    for(int i=0;i<4;i++){
        for(int j=i+1;j<4;j++){
            if(arr[j]<arr[i]){
                temp = arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
            }
        }
    }
    printf("Sorted array: ");
    for (int i = 0; i < 4; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;


}
