#include<iostream>
using namespace std;

void test(int *);
int main(){
    int A[]={1};
    test(A);
    cout<<A[0]<<endl;
    return 0;
}

void test(int * A){
    int i=111;
    A[0]=i;
}
