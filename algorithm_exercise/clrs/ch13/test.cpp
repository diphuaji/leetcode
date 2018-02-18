#include<iostream>
#include<string>
using namespace std;

class Index{
    public:
        double id;
};
class Hand{
    public:
        int i;
        Index index;
};
class Human{
    public:
        Hand hand;
};

Human getHuman(){
    Human c;
    Human h;
    cout<<"---inside func---"<<endl;
    cout<<"human addr: "<<&h<<endl;
    cout<<"hand addr: "<<&(h.hand)<<endl;
    cout<<"index addr: "<<&(h.hand.index)<<endl;
    return c;
}

void printText(string s){
    cout<<"s is: "<<s<<endl;
}

int main(){
    //Human h=getHuman();
    //cout<<"---outside func---"<<endl;
    //cout<<"human addr: "<<&h<<endl;
    //cout<<"hand addr: "<<&(h.hand)<<endl;
    //cout<<"index addr: "<<&(h.hand.index)<<endl;
    printText("xxx");
    string a,b,c;
    a=b=c=string("aaa");
    b+="bbb";
    string d="x"+c;
    cout<<"a: "<<a<<endl;
    cout<<"b: "<<b<<endl;
    cout<<"c: "<<c<<endl;
    cout<<"d: "<<d<<endl;
    return 0;
}
