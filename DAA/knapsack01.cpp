#include<iostream>
using namespace std;

int knapsack_01(int w1,int n,int p[],int wt[]){
    int k[n+1][w1+1];
    for(int i=0;i<=n;i++){
        for(int w = 0;w<=w1;w++){
            if(i==0 || w ==0)
                k[i][w] = 0;
            else if(wt[i]<=w)
                k[i][w] = max(k[i-1][w],k[i-1][w-wt[i]]+p[i]);
            else
                k[i][w] = k[i-1][w];
        }
    }
    cout<<"Weight by profit table :- "<<endl;
    for(int i=0;i<=n;i++){
        for(int j=0;j<=w1;j++){
            cout<<k[i][j]<<" ";
        }
        cout<<endl;
    }
    cout<<endl;
    // int i=n,j=w1;
    // while(i>0 || j>0){
    //     if(k[i][j]==k[i-1][j]){
    //         cout<<i<<" 0 "<<endl;
    //         i--;}
    //     else {
    //         cout<<i<<" 1 "<<endl;
    //         j =j-wt[i];
    //         i--;
    //     }
    // }
    // cout<<endl;
    return k[n][w1];
}

int main(){
    int w,n;
    cout<<"enter the size : ";
    cin>>n;
    cout<<"Enter the weight of the sack : ";
    cin>>w;
    int p[n],wt[n];
    p[0]=0,wt[0]=0;
    for(int i=1;i<=n;i++)
        cin>>p[i];
    for(int i=1;i<=n;i++)
        cin>>wt[i];
    int ans = knapsack_01(w,n,p,wt);
    cout<<ans<<endl;
}



/*
OUTPUT:-

Divyang@DESKTOP-EI8DDFC MINGW64 /c/users/divyang/Desktop/Trimester 8/DAA (master)
$ ./a.exe
enter the size : 4
Enter the weight of the sack : 8
1 2 5 6
2 3 4 5
Weight by profit table :- 
0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 1 1
0 0 1 2 2 3 3 3 3
0 0 1 2 5 5 6 7 7
0 0 1 2 5 6 6 7 8

8
*/
