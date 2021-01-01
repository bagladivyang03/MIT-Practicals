#include<iostream>
#include<bits/stdc++.h>
using namespace std;

struct Job{
    char label;
    int dead;
    int profit;
};

bool comparison(Job a, Job b){
    return (a.profit > b.profit);
}

void printSchedules (Job arr[], int n){

    sort(arr,arr+n,comparison);

    int result[n];
    bool slot[n]={false};


    for(int i=0;i<n;i++){

        for(int j=min(n,arr[i].dead)-1;j>=0;j--){
            if(slot[j]==false){
                result[j]=i;
                slot[j]=true;
                break;
            }
        }
    }

    for(int i=0;i<n;i++){
        if(slot[i])
            cout<<arr[result[i]].label<<" ";
    }
    cout<<endl;
}


int main(){
    int n;
    cout<<"Enter size : ";
    cin>>n;
    Job arr[n];
    for(int i=0;i<n;i++){
        cout<<"Enter the label/ID for Job "<<i+1<<" : ";
        cin>>arr[i].label;
        cout<<"Enter the deadline time for Job "<<i+1<<" : ";
        cin>>arr[i].dead;
        cout<<"Enter the profit for Job "<<i+1<<" : ";
        cin>>arr[i].profit;
    }

    printSchedules(arr,n);
}








/*

TIME COMPLEXITY :- O(n^2)
Enter size : 4
Enter the label/ID for Job 1 : a
Enter the deadline time for Job 1 : 4
Enter the profit for Job 1 : 20
Enter the label/ID for Job 2 : b
Enter the deadline time for Job 2 : 1
Enter the profit for Job 2 : 10
Enter the label/ID for Job 3 : c
Enter the deadline time for Job 3 : 1
Enter the profit for Job 3 : 40
Enter the label/ID for Job 4 : d
Enter the deadline time for Job 4 : 1
Enter the profit for Job 4 : 20
c a 
dbagla@DESKTOP-EI8DDFC:/mnt/c/users/divyang/Desktop/Trimester 8/DAA$

*/