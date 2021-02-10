#include<iostream>
#include<omp.h>
using namespace std;

long int partition(long int arr[],long int low,long int high){
    long int pivot = arr[high];
    long int i = low-1;
    for(long int j=low;j<=high;j++){
        if(arr[j]<pivot){
            i++;
            swap(arr[i],arr[j]);
        }
    }
    swap(arr[i+1],arr[high]);
    return i+1;
}

void parallel_quicksort(long int arr[],long int low,long int high){
    if(low<high){
        long int mid = partition(arr,low,high);

        #pragma omp parallel sections
        {
            #pragma omp section
            {
                parallel_quicksort(arr,low,mid-1);
            }
            #pragma omp section
            {
                parallel_quicksort(arr,mid+1,high);
            }
        }
    }
}

void serial_quicksort(long int arr[],long int low,long int high){
    if(low<high){
        long int mid = partition(arr,low,high);
        parallel_quicksort(arr,low,mid-1);
        parallel_quicksort(arr,mid+1,high);
    }
}


int main(){
    long int n;
    long int temp;
    cout<<"Enter the size of the array : ";
    cin>>n;
    long int arr[n];

    cout<<"Populating the array\n";

    int choice;
    cout<<"Is repetition alowed ? 1.Yes 0. No\n";
    cin>>choice;

    int choice1;
    cout<<"Enter the choice \n1.Serial Quick Sort \n2.Parallel Quick Sort \n";
    cin>>choice1;

    int flag = 0;
    if(choice==1){
        for(long int i=0;i<n;i++){
            arr[i] = (rand()%1000000);
        }
    }
    else{
        for(long int i=0;i<n;i++){
           flag = 0;
           int t = rand()%1000000;
           for(long int j=0;j<i;j++){
               if(arr[j]==t)
                    flag = 1;
           }
           if(flag==0)
                arr[i] = t;
            else
                i--;
        }
    }
    // cout<<"The Input array is :"<<endl;
    // for(long int i=0;i<n;i++){
    //     cout<<arr[i]<<" ";
    // }
    // cout<<endl;

    double start = omp_get_wtime();
    if(choice1==1){
        serial_quicksort(arr,0,n-1);
    }
    else if(choice1==2){
        parallel_quicksort(arr,0,n-1);        
    }
    else
    {
        cout<<"Invalid Choice !!"<<endl;
    }
    cout<<"The time required for execution is:"<<omp_get_wtime()-start<<endl;

    // cout<<"The Sorted array is :"<<endl;
    // for(long int i=0;i<n;i++){
    //     cout<<arr[i]<<" ";
    // }
    // cout<<endl;
}




/*
OUTPUT:-

dbagla@DESKTOP-EI8DDFC:/mnt/c/users/divyang/Desktop/Trimester 8/HPC/LABASSN5$ ./a.out
Enter the size of the array : 500
Populating the array
Is repetition alowed ? 1.Yes 0. No
1
Enter the choice
1.Serial Quick Sort
2.Parallel Quick Sort
1
The time required for execution is:0.0015797
dbagla@DESKTOP-EI8DDFC:/mnt/c/users/divyang/Desktop/Trimester 8/HPC/LABASSN5$ ./a.out
Enter the size of the array : 500
Populating the array
Is repetition alowed ? 1.Yes 0. No
1
Enter the choice
1.Serial Quick Sort
2.Parallel Quick Sort
2
The time required for execution is:0.0035536
dbagla@DESKTOP-EI8DDFC:/mnt/c/users/divyang/Desktop/Trimester 8/HPC/LABASSN5$ ./a.out
Enter the size of the array : 1000
Populating the array
Is repetition alowed ? 1.Yes 0. No
1
Enter the choice
1.Serial Quick Sort
2.Parallel Quick Sort
1
The time required for execution is:0.0028257
dbagla@DESKTOP-EI8DDFC:/mnt/c/users/divyang/Desktop/Trimester 8/HPC/LABASSN5$ ./a.out
Enter the size of the array : 1000
Populating the array
Is repetition alowed ? 1.Yes 0. No
1
Enter the choice
1.Serial Quick Sort
2.Parallel Quick Sort
2
The time required for execution is:0.0045662
dbagla@DESKTOP-EI8DDFC:/mnt/c/users/divyang/Desktop/Trimester 8/HPC/LABASSN5$ ./a.out
Enter the size of the array : 10000
Populating the array
Is repetition alowed ? 1.Yes 0. No
1
Enter the choice
1.Serial Quick Sort
2.Parallel Quick Sort
1
The time required for execution is:0.0172827
dbagla@DESKTOP-EI8DDFC:/mnt/c/users/divyang/Desktop/Trimester 8/HPC/LABASSN5$ ./a.out
Enter the size of the array : 10000
Populating the array
Is repetition alowed ? 1.Yes 0. No
1
Enter the choice
1.Serial Quick Sort
2.Parallel Quick Sort
2
The time required for execution is:0.0355079
dbagla@DESKTOP-EI8DDFC:/mnt/c/users/divyang/Desktop/Trimester 8/HPC/LABASSN5$ ./a.out
Enter the size of the array : 30000
Populating the array
Is repetition alowed ? 1.Yes 0. No
1
Enter the choice
1.Serial Quick Sort
2.Parallel Quick Sort
1
The time required for execution is:0.0457119
dbagla@DESKTOP-EI8DDFC:/mnt/c/users/divyang/Desktop/Trimester 8/HPC/LABASSN5$ ./a.out
Enter the size of the array : 30000
Populating the array
Is repetition alowed ? 1.Yes 0. No
0
Enter the choice
1.Serial Quick Sort
2.Parallel Quick Sort
2
The time required for execution is:0.0395813
dbagla@DESKTOP-EI8DDFC:/mnt/c/users/divyang/Desktop/Trimester 8/HPC/LABASSN5$
dbagla@DESKTOP-EI8DDFC:/mnt/c/users/divyang/Desktop/Trimester 8/HPC/LABASSN5$ ./a.out
Enter the size of the array : 50000
Populating the array
Is repetition alowed ? 1.Yes 0. No
1
Enter the choice
1.Serial Quick Sort
2.Parallel Quick Sort
1
The time required for execution is:0.0635719
dbagla@DESKTOP-EI8DDFC:/mnt/c/users/divyang/Desktop/Trimester 8/HPC/LABASSN5$ ./a.out
Enter the size of the array : 50000
Populating the array
Is repetition alowed ? 1.Yes 0. No
1
Enter the choice
1.Serial Quick Sort
2.Parallel Quick Sort
2
The time required for execution is:0.0832434
dbagla@DESKTOP-EI8DDFC:/mnt/c/users/divyang/Desktop/Trimester 8/HPC/LABASSN5$ ./a.out
Enter the size of the array : 70000
Populating the array
Is repetition alowed ? 1.Yes 0. No
1
Enter the choice
1.Serial Quick Sort
2.Parallel Quick Sort
1
The time required for execution is:0.0811113
dbagla@DESKTOP-EI8DDFC:/mnt/c/users/divyang/Desktop/Trimester 8/HPC/LABASSN5$ ./a.out
Enter the size of the array : 70000
Populating the array
Is repetition alowed ? 1.Yes 0. No
0
Enter the choice
1.Serial Quick Sort
2.Parallel Quick Sort
2

^C
dbagla@DESKTOP-EI8DDFC:/mnt/c/users/divyang/Desktop/Trimester 8/HPC/LABASSN5$ ./a.out
Enter the size of the array : 70000
Populating the array
Is repetition alowed ? 1.Yes 0. No
0
Enter the choice
1.Serial Quick Sort
2.Parallel Quick Sort
2
The time required for execution is:0.106054
dbagla@DESKTOP-EI8DDFC:/mnt/c/users/divyang/Desktop/Trimester 8/HPC/LABASSN5$ ./a.out
Enter the size of the array : 100000
Populating the array
Is repetition alowed ? 1.Yes 0. No
1
Enter the choice
1.Serial Quick Sort
2.Parallel Quick Sort
1
The time required for execution is:0.115438
dbagla@DESKTOP-EI8DDFC:/mnt/c/users/divyang/Desktop/Trimester 8/HPC/LABASSN5$ ./a.out
Enter the size of the array : 100000
Populating the array
Is repetition alowed ? 1.Yes 0. No
0
Enter the choice
1.Serial Quick Sort
2.Parallel Quick Sort
2
The time required for execution is:0.111286
dbagla@DESKTOP-EI8DDFC:/mnt/c/users/divyang/Desktop/Trimester 8/HPC/LABASSN5$

*/