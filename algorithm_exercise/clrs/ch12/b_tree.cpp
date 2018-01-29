#include<iostream>
#include<vector>
using namespace std;

struct node{
    node & left;
    node & right;
    node & parent;
};
void insert();
void deletion();
void transplant();

int main(){
    vector<int> v1;
    v1.push_back(9);
    vector<int> v2=v1;
    v2.push_back(19);
    cout<<"size of v1:"<<v1.size()<<endl;
    cout<<"size of v2:"<<v2.size()<<endl;
    return 0;
}
