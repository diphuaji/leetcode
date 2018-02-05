#include<iostream>
#include<vector>
using namespace std;

struct Node{
    int key; 
    Node * left=NULL;
    Node * right=NULL;
    Node * p=NULL;
};
struct BTree{
    Node * root=NULL;
};
void printTree(BTree *);
Node * getMinimum(BTree *);
Node * getSuccessor(Node *);
Node * search(BTree *,int key);
void insert(BTree *,int);
void del(BTree *,int);
void del(BTree *,Node *);
void transplant(BTree *,Node *,Node *);

int main(){
    BTree tree;
    int l[]={8,2,3,1,22,3,0,9,8,-23};
    for(int i=0;i<10;i++){
        insert(&tree,l[i]);
    }
    printTree(&tree);
    del(&tree,8);
    printTree(&tree);
    del(&tree,22);
    printTree(&tree);
    del(&tree,-12);
    printTree(&tree);
    del(&tree,2);
    printTree(&tree);
    del(&tree,-23);
    printTree(&tree);
    return 0;
}

void printTree(BTree * tree){
    Node * node = getMinimum(tree);
    cout<<"tree:"<<endl;
    while(node){
        cout << node->key<<","<<endl;
        node=getSuccessor(node);
    }
    cout<<"---"<<endl;
}

Node * getMinimum(BTree * tree) {
    Node * root=tree->root;
    if(!root) return NULL;
    while(root->left){
        root=root->left;
    }
    return root;
}

Node * getSuccessor(Node * node){
    if(!node) return NULL;    
    if(node->right){
        node=node->right;
        while(node->left){
            node=node->left;
        }
        return node;
    }
    while(node){
        if(!node->p) return NULL;
        if(node==node->p->left) return node->p;
        node = node->p;
    }
}

Node * search(BTree * tree,int key){
    Node * node=tree->root;
    while(node){
        if(key==node->key) return node;
        if(key<node->key){
            node=node->left;
            continue;
        }
        node=node->right;
    }
    return node;
}

void insert(BTree * tree,int key){
    cout<<"inserting "<<key<<endl;
    Node * c=new Node;
    c->key=key;
    if (!tree->root){
        tree->root=c;
        return;
    }
    Node * p=tree->root;
    while (true){
        if (key<p->key){
            if(!p->left) {
                c->p=p;
                p->left=c;
                break;
            }
            p=p->left;
            continue;
        }
        if(!p->right) {
            c->p=p;
            p->right=c;
            break;
        }
        p=p->right;
    }
}

void del(BTree * tree,int key){
    del(tree,search(tree,key));
}

void del(BTree * tree,Node * node){
    if(!node) return;
    if(!node->left&&!node->right){
        if(node->p){
            if(node==node->p->left){
                node->p->left=NULL;
                return;
            }
            node->p->right=NULL;
            return;
        }
        //it's the root
        tree->root=NULL;
        delete node;
        return;
    }
    if(node->left && node->right){
        Node * tmp=node;
        node=node->right;
        while(node->left){
            node=node->left;
        }
        tmp->key=node->key;
        del(tree,node);
        return;
    }
    if(node->left){
        transplant(tree,node,node->left);
        delete node;
        return;
    }
    transplant(tree,node,node->right);
    delete node;
}

void transplant(BTree * tree,Node * oldNode,Node * node){
    if(!oldNode->p){
        tree->root=node;
    }else if(oldNode==oldNode->p->left){
        oldNode->p->left=node;
    }else{
        oldNode->p->right=node;
    }
    if(node!=NULL){
        node->p=oldNode->p;
    }
}
