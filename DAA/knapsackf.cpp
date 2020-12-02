#include<bits/stdc++.h>

struct Item{
    int value,weight; 
};
// for comapring the value/weight and sorting acc to the descending order
bool cmp(struct Item r1,struct Item r2){
    double a = (double)r1.value/(double)r1.weight;
    double b = (double)r2.value/(double)r2.weight;
    return a>b;
}

int knapsackfraction(struct Item arr[],int n,int w){
    std::sort(arr,arr+n,cmp);
    int currweight = 0,finalans = 0;
    // iterating to whole array and taking values
    for(int i=0;i<n;i++){
        // if adding the weight at i position doesn't makes greater than total weight
        if(currweight + arr[i].weight <= w){
            currweight += arr[i].weight;
            finalans += arr[i].value;
        }
        // if weight becomes more then we hust take the fraction of that and break from the loop
        else{
            int remWeight = w - currweight;
            finalans += arr[i].value*((double)remWeight/(double)arr[i].weight);
            break;
        }
    }
    //returing the final ans
    return finalans;
}

int main(){
    int w;
    std::cout<<"Enter the weight of knapsack: ";
    std::cin>>w;
    int n;
    std::cout<<"Enter the value of n: ";
    std::cin>>n;
    Item arr[n];
    for(int i=0;i<n;i++){
        std::cout<<"Enter the value and weight for item "<<i+1<<": ";
        std::cin>>arr[i].value;
        std::cin>>arr[i].weight;
    }
    std::cout<<"Weight"<<" "<<"Value"<<"\n";
    for(int i=0;i<n;i++){
        std::cout<<arr[i].weight<<" "<<arr[i].value<<"\n";
    }
    std::cout<<"Maximum value obtained is "<<knapsackfraction(arr,n,w)<<"\n";
}


/*
OUTPUT :-

Enter the weight of knapsack: 100
Enter the value of n: 5 
Enter the value and weight for item 1: 20 10
Enter the value and weight for item 2: 30 20
Enter the value and weight for item 3: 66 30
Enter the value and weight for item 4: 40 40 
Enter the value and weight for item 5: 60 50
Weight Value
10 20
20 30
30 66
40 40
50 60
Maximum value obtained is 164
dbagla@DESKTOP-EI8DDFC:/mnt/c/users/divyang/Desktop/Trimester 8/DAA$ 
*/
