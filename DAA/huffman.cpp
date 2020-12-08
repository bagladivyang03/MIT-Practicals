#include<iostream>
#include<bits/stdc++.h>
using namespace std;


//declared structure for heap with fields for data and its frequency
struct minHeapNode {
    char data;
    unsigned freq;
    minHeapNode *left, *right;
    minHeapNode(char data,unsigned freq){
        left=right=NULL;
        this->data=data;
        this->freq=freq;
    }
};


//for comparison to make the minheap
struct compare{
    bool operator()(minHeapNode *l1, minHeapNode *l2){
        return (l1->freq > l2->freq);
    }
};


//printing all the codes 
void printnodes(struct minHeapNode* root,string str ){
    if(!root)
        return;
    //if data is not '#' then print the data and its code
    if(root->data!='#')
        cout<<root->data<<" : "<< str <<endl;
    
    //recursively calling if left part of data then add "0" else "1" in str
    printnodes(root->left,str+"0");
    printnodes(root->right,str+"1");
}

//function for huffman code
void huffmanCodes(char data[],int freq[],int size){
    struct minHeapNode *left,*right,*top;

    //declaring the priority queue as minheap
    priority_queue<minHeapNode* ,vector<minHeapNode*>,compare> minHeap;

    // pushing all the data ad frequency in minheap i.e priority_queue
    for(int i=0;i<size;i++){
        minHeap.push(new minHeapNode(data[i],freq[i]));
    }

    //running the loop till the size doesnt become 1
    while(minHeap.size()!=1){
        left = minHeap.top();
        minHeap.pop();

        right = minHeap.top();
        minHeap.pop();

        //poppinf out the smallest two freq and adding it and pushing with a '#' only
         top = new minHeapNode('#',left->freq+right->freq);

        // left and right part get connected to top
        top->left = left;
        top->right = right;

        minHeap.push(top);
    }

    //printing the codes
    printnodes(minHeap.top(),"");

}


int main(){
    char arr[] = {'A','B','C','D','E'};
    int freq[] = {5,9,12,13,16};
    int size = sizeof(arr)/sizeof(arr[0]);

    huffmanCodes(arr,freq,size);

return 0;
}