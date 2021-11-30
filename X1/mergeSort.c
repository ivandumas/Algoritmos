#include<stdlib.h>
#include<stdio.h>

void merge(int arr[],int left, int m, int right);

void mergeSort(int arr[], int left, int right){

    if (left < right){
        int m = left+(right-left)/2;
        mergeSort(arr,left,m);
        mergeSort(arr,m+1,right);
        merge(arr,left,m,right);
    }
}

void merge(int arr[],int left, int m, int right){
    int i, j, k;
    int n1 = m - left + 1;
    int n2 =  right - m;

    int L[n1], R[n2]; //Auxiliary arrays

    for (i = 0 ; i < n1 ; i++) L[i] = arr[left + i];
    for (j = 0 ; j < n2 ; j++) R[j] = arr[m + 1 + j];

    i = 0; j=0; k = left;

    while (i < n1 && j < n2){
        if (L[i] <= R[j]){
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        arr[k] = L[i];
        i++;k++;
    }

    while (j < n2) {
        arr[k] = R[j];
        j++;k++;
    }
}


int main(void) {
    int arr[] = {18,5,4,17,30,12,24,4,3,6};
    int right = sizeof(arr)/sizeof(arr[0]);
    int i;
    for (i=0; i < right; i++)
        printf("%d ", arr[i]);
    printf("\n");

    mergeSort(arr,0,right-1);
    for (i=0; i < right; i++)
        printf("%d ", arr[i]);
    printf("\n");
    return 0;
}