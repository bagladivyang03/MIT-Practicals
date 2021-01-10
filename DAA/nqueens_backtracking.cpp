/*
NAME:- Divyang Bagla
PANEL:- D (D2)
ROLL NO.:- PD32
SUBJECT:- DAA
*/

#include<bits/stdc++.h>
using namespace std;

bool place(int k,int col,int arr[]){
    for(int j=0;j<k;j++){
        if((arr[j]==col) || (abs(arr[j]-col)== abs(j-k)))
            return false;
    }
    return true;
}

void Nqueen(int k,int n,int arr[]){
    for(int col=0;col<n;col++){
        if(place(k,col,arr)){
            arr[k] = col;
            if(k==n-1)
            {
                for(int i=0;i<n;i++){
                    cout<<arr[i]+1<<" ";
                }
                cout<<endl;
                for(int i=0;i<n;i++){
                    for(int j=0;j<n;j++){
                        if(arr[i]==j)
                            cout<<"Q"<<" ";
                        else
                            cout<<"."<<" ";
                    }
                    cout<<endl;
                }
                cout<<"=========================="<<endl;
                break;
            }
            else Nqueen(k+1,n,arr);
        }
    }
}

int main(){
    int n;
    cout<<"Enter the total no. of Queens"<<endl;
    cin>>n;
    int arr[n];
    Nqueen(0,n,arr);

}


/*
OUTPUT:-
Divyang@DESKTOP-EI8DDFC MINGW64 /c/users/divyang/DEsktop/Trimester 8/DAA (master)
$ ./a.exe
Enter the total no. of Queens
4
2 4 1 3 
. Q . .
. . . Q
Q . . .
. . Q .
==========================
3 1 4 2
. . Q .
Q . . .
. . . Q
. Q . .
==========================
*/