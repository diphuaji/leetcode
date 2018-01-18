#include<iostream>
using namespace std;

void quickSort(int *,int,int);
int partition(int *,int,int);

int main(){
    int A[]={2,5,1,2,8,3,1,15,23,555,1,5,3,98,54,76,8,45,31};
    int r = 18;
    quickSort(A,0,r);
    for(int n=r;n>-1;n--){
        cout << A[r-n] << ", ";
    }
    cout << endl;
    return 0; 
}

//r is in index in the A
void quickSort(int * A,int p,int r){
    if(p>=r) return;
    int q=partition(A,p,r);
    quickSort(A,p,q-1);
    quickSort(A,q+1,r);
}

int partition(int * A,int p,int r){
    int i=p-1;
    //for(int n=5;n>-1;n--){
    //    cout << A[5-n] << ", ";
    //}
    //cout << endl;
    for(int j=p;j<r;j++){
        if (A[j]<=A[r]){
            i++;
            int tmp=A[j];
            A[j]=A[i];
            A[i]=tmp;
        }
    }   
    int tmp=A[r];
    A[r]=A[i+1];
    A[i+1]=tmp;
    return i+1;
}
