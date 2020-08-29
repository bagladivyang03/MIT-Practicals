#include <iostream>
using namespace std;
void cal_distance(int c[100][100] , int s ,int n); //function created for calculating smallest path from starting position
void cal_distance(int c[100][100] , int s ,int n){
    int d[n] , start,temp;
    d[s]=0;
    for(int i=0;i<n;i++){            
        if(i==s)
            continue;
        else
            d[i] = 100;
    }
    for(int k=0;k<n-1;k++){
        temp = 0;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(c[i][j]!=100 && c[i][j]!=0){     //if distance is 0 and 100 then direct path not available
                    if(d[i]+c[i][j]<d[j]){                       
                        d[j] = d[i]+c[i][j];
                        temp = 1;
                    }
                }
            }
        }
        if(temp ==0)
            break;
    }
    cout<<"shortest routes from "<<s<<" are :"<<endl;       //displaying all the paths from starting position
    for(int i=0;i<n;i++)
    {
        cout<<s<<" to "<<i<<" = "<<d[i]<<endl;
    }
}
int main()
{
    int n;
    cout<<"Enter the total no. of Routers "; //accepting the no of routers 
    cin>>n;
    int c[100][100] , i ,j;
    for(i=0;i<n;i++){                          //accepting the distance matrix
        for(j=0;j<n;j++){
            cout<<"Enter the cost from "<<i<<" to "<<j<<" :";
            cin>>c[i][j];
        }
    }
    
    for(int i=0;i<n;i++){                //calling for each and every node
        cal_distance(c,i,n);
    }
    return 0;
}

/*
Enter the total no. of Routers 4                                                                                  
Enter the cost from 0 to 0 :0                                                                                     
Enter the cost from 0 to 1 :3                                                                                     
Enter the cost from 0 to 2 :0                                                                                     
Enter the cost from 0 to 3 :6
Enter the cost from 1 to 0 :3                                                                                     
Enter the cost from 1 to 1 :0                                                                                     
Enter the cost from 1 to 2 :4                                                                                     
Enter the cost from 1 to 3 :8                                                                                     
Enter the cost from 2 to 0 :0
Enter the cost from 2 to 1 :4                                                                                     
Enter the cost from 2 to 2 :0                                                                                     
Enter the cost from 2 to 3 :5                                                                                     
Enter the cost from 3 to 0 :6                                                                                     
Enter the cost from 3 to 1 :8
Enter the cost from 3 to 2 :5                                                                                     
Enter the cost from 3 to 3 :0                                                                                     
shortest routes from 0 are : 
0 to 0 = 0                                                                                                        
0 to 1 = 3                                                                                                        
0 to 2 = 7                                                                                                        
0 to 3 = 6
shortest routes from 1 are :                                                                                      
1 to 0 = 3                                                                                                        
1 to 1 = 0                                                                                                        
1 to 2 = 4 
1 to 3 = 8                                                                                                        
shortest routes from 2 are :                                                                                      
2 to 0 = 7
2 to 1 = 4                                                                                                        
2 to 2 = 0                                                                                                        
2 to 3 = 5
shortest routes from 3 are :                                                                                      
3 to 0 = 6                                                                                                        
3 to 1 = 8                                                                                                        
3 to 2 = 5                                                                                                        
3 to 3 = 0
*/
