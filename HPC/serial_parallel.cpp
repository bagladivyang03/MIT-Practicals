#include<iostream>
#include<omp.h>

int main(){
    omp_set_num_threads(2);
    std::cout<<"Enter the number :";
    int n;
    std::cin>>n;
    int s1 = 0,ss=0;
    std::cout<<"Sequential code"<<"\n";
    for(int i=1;i<=n;i++){
        ss += i;
        std::cout<<ss<<"\n";
    }
    std::cout<<"Sum is ";
    std::cout<<ss<<"\n";
    std::cout<<"Parallelization of above loop "<<"\n";
    #pragma omp parallel for
    for(int i=1;i<=n;i++){
        s1 +=i;
        std::cout<<s1<<"\n";
    }
    std::cout<<"Sum is ";
    std::cout<<s1<<"\n";
return 0;
}


/*
Enter the number :5
Sequential code
1
3
6
10
15
Sum is 15
Parallelization of above loop 
1
7
10
5
15
Sum is 15
*/


