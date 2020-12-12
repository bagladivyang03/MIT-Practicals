//To make the code run properly pls take tha size of array too large like more than 30k size.

#include<iostream>
#include<bits/stdc++.h>
#include<omp.h>
using namespace std;


int main(){
    unsigned long long int size;
    unsigned long long int temp;
    size = 5;
    cout<<"Enter the size : ";
    cin>>size;
    unsigned long long int arr_par[size] ;
    unsigned long long int arr_ser[size] ;
    #pragma omp for
    for(unsigned long long int i=0;i<size;i++){
        arr_par[i] = size-i;
        arr_ser[i] = size-i;
    }
    // double start, end;

    //serial bubble sort
    double start = omp_get_wtime();
    for(unsigned long long int i=0;i<size-1;i++){
        for(unsigned long long int j=0;j<size-i-1;j++){
            if(arr_ser[j] > arr_ser[j+1]){
                swap(arr_ser[j],arr_ser[j+1]);
            }
        }
    }
    double end = omp_get_wtime();
    cout<<"Array sorted after serial excecution :"<<endl;
    for(unsigned long long int i=0;i<size;i++)
        cout<<arr_ser[i]<<" ";
    cout<<endl;
    cout<<"Time for serial execution "<<(end-start)<<endl;

    //parallel bubble sort
    unsigned long long int first;
    double start1 = omp_get_wtime();
    for(unsigned long long int k=0;k<=size/2;k++){

        #pragma omp parallel for 
        for(unsigned long long int j=1;j<size-1;j+=2){
            if(arr_par[j]>arr_par[j+1]){   
                swap(arr_par[j],arr_par[j+1]);
            }
        }

        #pragma omp parallel for
        for(unsigned long long int i=0;i<size-1;i+=2){
            if(arr_par[i]>arr_par[i+1]){
                swap(arr_par[i],arr_par[i+1]);                
            }
        }
    }
    double end1 = omp_get_wtime();
    cout<<"Array sorted after parallel excecution :"<<endl;
    for(unsigned long long int i=0;i<size;i++)
        cout<<arr_par[i]<<" ";
    cout<<endl;
    cout<<"Time for parallel execution "<<(end1-start1)<<endl;

return 0;
}





