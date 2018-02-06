#include<iostream>
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

int main(){
    Human h=getHuman();
    cout<<"---outside func---"<<endl;
    cout<<"human addr: "<<&h<<endl;
    cout<<"hand addr: "<<&(h.hand)<<endl;
    cout<<"index addr: "<<&(h.hand.index)<<endl;
    
    return 0;
}
