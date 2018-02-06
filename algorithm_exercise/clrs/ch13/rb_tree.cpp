#include<iostream>
using namespace std;

class RBNode{
    public:
        int key;
        RBNode * p=NULL;
        RBNode * l=NULL;
        RBNode * r=NULL;
};
class RBTree{
    public:
        RBNode * root;
        RBNode * nil;
        void printTree();
        RBNode * getMinimum(RBNode*);
        RBNode * getMinimum();
        RBNode * search(int);
        RBNode * del(RBNode);
        RBNode * transplant(RBNode*);
        RBNode * getSuccessor(RBNode*);
        RBNode * insert(int);
};


void RBTree::printTree(){
    RBNode * node=getMinimum(this->root);
    cout << "Tree:"<<endl;
    while(node!=this->nil){
        cout<<node->key<<endl;
        node=this->getSuccessor(node);
    }
}


RBNode * RBTree::getMinimum(RBNode * node){
    if(node==this->nil) return this->nil;
    while(node->l!=this->nil){
        node=node->l;
    }
    return node;
}

RBNode * RBTree::getMinimum(){
    RBNode * node = this->root;
    if(node==this->nil) return this->nil;
    while(node->l!=this->nil){
        node=node->l;
    }
    return node;
}

RBNode * RBTree::search(int key){
    RBNode * node=this->root;
    while(node!=this->nil){
        if(key==node->key) return node;
        if(key<node->key){
            node=node->l;
            continue;
        }
        node=node->r;
    }
    return node;
}

RBNode * RBTree::getSuccessor(RBNode * node){
    if(node==this->nil) return this->nil; 
    if(node->r){
        node=node->r;
        while(node->l){
            node=node->l;
        }
        return node;
    }
    while(node!=this->nil){
        if(!node->p) return this->nil;
        if(node==node->p->l) return node->p;
        node = node->p;
    }
}

int main(){
    RBTree tree;

    return 0;
}

