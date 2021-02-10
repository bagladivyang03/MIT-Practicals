#include<iostream>
using namespace std;

int partition(int arr[],int l,int h){
    int pivot = arr[h];
    int i = l-1;

    for(int j=l;j<=h;j++){
        if(arr[j]<pivot){
            i++;
            swap(arr[i],arr[j]);
        }
    }
    swap(arr[i+1],arr[h]);
    return i+1;

}

void quicksort(int arr[],int l,int h){
    if(l<h){
        int r = l + rand()%(h-l+1);
        swap(arr[r],arr[h]);
        int pi = partition(arr,l,h);

        quicksort(arr,l,pi-1);
        quicksort(arr,pi+1,h);

    }
}

int main(){
    int n;
    cout<<"Enter the no of the elements";
    cin>>n;
    int arr[n];
    cout<<"Enter the elemets in array";
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    cout<<"Array before sorting"<<endl;
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    quicksort(arr,0,n-1);
    cout<<"Array after sorting"<<endl;
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;

}