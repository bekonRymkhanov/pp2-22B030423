#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int a, b, c;
    cin>>a>>b>>c;
    if((a%2==0 && b%2==0 && c%2==0) || (a%2==1 && b%2==1 && c%2==1)){
       cout<<"No";
    }
    else{
        cout<<"Valid";
    }
    return 0;
}