#include<bits/stdc++.h>

void merge(int arr[],int start,int mid,int last){
    int s1 = mid - start + 1;
    int s2 = last - mid;
    int a[s1],b[s2];
    for(int i=0;i<s1;i++)
        a[i] = arr[start+i];
    for(int i=0;i<s2;i++)
        b[i] = arr[mid + i +1];
    
    int index1 = 0,index2 = 0,k=start;
    while(index1 < s1 && index2 < s2){
        if(a[index1]<=b[index2]){
            arr[k]=a[index1];
            index1++;
        }
        else{
            arr[k]=b[index2];
            index2++;
        }
        k++;
    }
    while(index1 < s1){
        arr[k] = a[index1];
        index1++;
        k++;
    }
    while(index2 < s2){
        arr[k] = b[index2];
        index2++;
        k++;
    }
}

void mergesort(int arr[],int l,int h){
    if(l < h){
        int mid = (l+h)/2;
        mergesort(arr,l,mid);
        mergesort(arr,mid+1,h);
        merge(arr,l,mid,h);
    }
}
int main(){
    int n;
    std::cout<<"Enter the total no. of elements : ";
    std::cin>>n;
    int arr[n];
    for(int i=0;i<n;i++)
        std::cin>>arr[i];
    std::cout<<"Array before sorting : ";
    for(int i=0;i<n;i++)
        std::cout<<arr[i]<<" ";  
    std::cout<<"\n";
    mergesort(arr,0,n-1); 
    std::cout<<"Array after sorting : ";
    for(int i=0;i<n;i++)
        std::cout<<arr[i]<<" ";
    std::cout<<"\n";  

return 0;
}