#include<stdio.h>
#include<stdlib.h>
#include<omp.h>

void generate(char* filename, long long int size){
    FILE *file = fopen(filename,"w");

    for(long long int i=0;i<size;i++){
        fprintf(file, "%lld ", rand());
    }
    fclose(file);
}


void read(FILE *file,long long int size,long long int *arr){
    for(long long int i=0;i<size;i++){
        fscanf(file,"%lld",&arr[i]);
    }
}

int main(){
    long long int size;
    printf("Enter the size of arrays :");
    scanf("%lld",&size);

    //generating input files
    #pragma omp parallel sections
    {
        #pragma omp section
        {
            generate("input1.txt",size);
        }
        #pragma omp section
        {
            generate("input2.txt",size);
        }
    }

    FILE *file1 = fopen("input1.txt","r");
    FILE *file2 = fopen("input2.txt","r");
    FILE *op = fopen("outputparallel.txt","w");
    FILE *op1 = fopen("outputserial.txt","w");

    long long int arr1[size],arr2[size],sum[size];

    //PARALLEL EXECUTION
    double start = omp_get_wtime();
    #pragma omp parallel sections
    {
        #pragma omp section
        {
            read(file1,size,arr1);
        }
        #pragma omp section
        {
            read(file2,size,arr2);
        }
    }

    #pragma omp parallel for
    for(long long int i=0;i<size;i++){
        sum[i] = arr1[i] + arr2[i];
    }

    for(long long int i=0;i<size;i++){
        fprintf(op,"%lld ",sum[i]);
    }

    printf("Parallel Time: %f\n",omp_get_wtime()-start);

    // END PARALLEL EXECUTION

    //SERIAL EXECUTION

    start = omp_get_wtime();

    read(file1,size,arr1);
    read(file2,size,arr2);

    for(long long int i=0;i<size;i++){
        sum[i] = arr1[i] + arr2[i];
    }

    for(long long int i=0;i<size;i++){
        fprintf(op1,"%lld ",sum[i]);
    }

    printf("Serial execution: %f\n",omp_get_wtime()-start);

    //END SERIAL EXECUTION

    fclose(file1);
    fclose(file2);

return 0;


}


/*
OUTPUT:-
dbagla@DESKTOP-EI8DDFC:/mnt/c/users/divyang/Desktop/Trimester 8/HPC/LABASSN4$ ./a.out
Enter the size of arrays :100000
Parallel Time: 0.137269
Serial execution: 3.264022
*/