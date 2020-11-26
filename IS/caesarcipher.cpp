#include<iostream>
using namespace std;
string encrpyt(string s,int shift){
    string ans = "";
    for(int i=0;i<s.length();i++){
        if(isupper(s[i])){
            ans += char(int(s[i]+shift-65)%26 + 65);
        }
        else{
            ans += char(int(s[i]+shift-97)%26 + 97);
        }
    }
    return ans;

}
string decrypt(string s,int shift){
    string ans = "";
    for(int i=0;i<s.length();i++){
        // cout<<int(s[i]-shift-97)%26<<endl;
        if(isupper(s[i])){
            int k = int(s[i]-shift-65)%26;
            if(k < 0)
                ans += char(k + 26 + 65);
            else
               ans += char(k + 65); 
        }
        else{
            int k = int(s[i]-shift-97)%26;
            if(k < 0)
                ans += char(k + 26 + 97);
            else
               ans += char(k + 97); 
        }
    }
    return ans;
}
int main(){
    string s;
    int shift;
    cout<<"Enter the string to be encrypted"<<endl;
    cin>>s;
    cout<<"Enter the no. of shifts to be made"<<endl;
    cin>>shift;
    string ans = encrpyt(s,shift);
    cout<<"The encrypted string is :";
    cout<<ans<<endl;
    string decans = decrypt(ans,shift);
    cout<<"The decrypted string is :";
    cout<<decans<<endl;
}







/*
OUTPUT :- 
dbagla@DESKTOP-EI8DDFC:/mnt/c/users/divyang/Desktop/Trimester 8/IS$ g++ caesarcipher.cpp
dbagla@DESKTOP-EI8DDFC:/mnt/c/users/divyang/Desktop/Trimester 8/IS$ ./a.out
Enter the string to be encrypted
mitwpu
Enter the no. of shifts to be made
4
The encrypted string is :qmxaty
The decrypted string is :mitwpu

*/

