#include<bits/stdc++.h>
using namespace std;
#define MAX 10

void printboard(int board[MAX][MAX], int n){
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cout<<board[i][j]<<" ";
        }
        cout<<endl;
    }
    cout<<endl;
}

bool isSafe(int board[MAX][MAX],int row, int col,int n){
    int i,j;

    for(i=0;i<col;i++)
        if(board[row][i])
            return false;
    for(i=row,j=col;i>=0 && j>=0;i--,j--)
        if(board[i][j])
            return false;

    for(i=row,j=col;j>=0 && i<n;i++,j--)
        if(board[i][j])
            return false;  

    return true;  
}

bool solveNQUtil(int board[MAX][MAX],int n,int col){
    if(col>=n)
        return true;
    for(int i=0;i<n;i++){
        if(isSafe(board,i,col,n)){
            board[i][col] = 1;

            if(solveNQUtil(board,n,col+1))
                return true;
            
            board[i][col] = 0;
        }
    }
    return false;
}
int main(){
    int n;
    cout<<"Enter the total no. of queens : ";
    cin>>n;
    int board[MAX][MAX];
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            board[i][j]=0;
    if(solveNQUtil(board,n,0)==false)
    {
        cout<<"Solution doesn't exsists !!"<<endl;
    }
    else
    {
        printboard(board,n);
    }
    
}

/*

OUTPUT:-
Enter the total no. of queens : 5
1 0 0 0 0 
0 0 0 1 0
0 1 0 0 0
0 0 0 0 1
0 0 1 0 0

*/

