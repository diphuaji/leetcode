#include<iostream>
#include<string>
using namespace std;

enum Color{red,black};

class RBNode{
    public:
        RBNode();
        int key;
        RBNode * p;
        RBNode * l;
        RBNode * r;
        Color c;
};

RBNode::RBNode(){
    key=-1;
    c=red;
    this->p=NULL;
    this->l=NULL;
    this->r=NULL;
}

class RBTree{
    public:
        RBTree();
        RBNode * root;
        RBNode * nil;
        void prettyPrint();
        void prettyPrint(string,bool,RBNode *);
        void printTree();
        RBNode * getMinimum(RBNode*);
        RBNode * getMinimum();
        RBNode * search(int);
        void del(RBNode*);
        void delFix(RBNode*);
        void transplant(RBNode*,RBNode*);
        RBNode * getSuccessor(RBNode*);
        void rightRotate(RBNode *);
        void leftRotate(RBNode *);
        void insert(int);
        void insertFix(RBNode * );
};

RBTree::RBTree(){
    root=nil=new RBNode;
    nil->c=black;
    root->p=root->l=root->r=nil;
}

void RBTree::prettyPrint(){
    this->prettyPrint("",true,this->root);
}

void RBTree::prettyPrint(string prefix,bool isTail, RBNode * node){
    if(node==this->nil) return;
    string suffix="";
    this->prettyPrint(prefix+(isTail ?"│   " : "    "),false,node->r);
    cout<<prefix<<(isTail ? "└── ":"┌── ")<<node->key<<","<<node->c<<suffix<<endl;
    this->prettyPrint(prefix+(isTail ?"    ":"│   "),true,node->l);
    //if(node==this->nil){
    //    cout<< prefix<<(isTail ? "└── " : "├── ") << endl;
    //    return;
    //}
    //cout<< prefix << (isTail ? "└── " : "├── ") << node->key<<","<<node->c<<endl;
    //if (node->r==this->nil && node->l==this->nil) return;
    //this->prettyPrint(prefix+(isTail ? "    " : "│   "),false,node->r);
    //this->prettyPrint(prefix+(isTail ? "    " : "│   "),true,node->l);
}

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
        return this->getMinimum(node->r);
    }
    while(node!=this->nil){
        if(!node->p) return this->nil;
        if(node==node->p->l) return node->p;
        node = node->p;
    }
}

void RBTree::transplant(RBNode * oldNode,RBNode * newNode){
    if(oldNode==this->root) this->root=newNode;
    if(oldNode==oldNode->p->l){
        oldNode->p->l=newNode;
    }else{
        oldNode->p->r=newNode;
    }
    newNode->p=oldNode->p;
}

void RBTree::rightRotate(RBNode * z){
    //cout<<"before right rotating: "<<z->key<<endl;
    //this->prettyPrint();
    if(z==this->root) this->root=z->l;
    if(z->l==this->nil) return;
    z->l->p=z->p;
    if(z!=this->root){
        if(z==z->p->l){
            z->p->l=z->l;
        }else{
            z->p->r=z->l;
        }
    }
    RBNode * branch=z->l->r;
    z->l->r=z;
    z->p=z->l;
    z->l=branch;
    branch->p=z;
    //cout<<"after right rotating: "<<z->key<<endl;
    //this->prettyPrint();
}

void RBTree::leftRotate(RBNode * z){
    //cout<<"before left rotating: "<<z->key<<endl;
    //this->prettyPrint();
    if(z==this->root) this->root=z->r;
    if(z->r==this->nil) return;
    z->r->p=z->p;
    if(z!=this->root){
        if(z==z->p->l){
            z->p->l=z->r;
        }else{
            z->p->r=z->r;
        }
    }
    RBNode * branch=z->r->l;
    z->r->l=z;
    z->p=z->r;
    z->r=branch;
    branch->p=z;
    //cout<<"after left rotating: "<<z->key<<endl;
    //this->prettyPrint();
}

void RBTree::insert(int key){
    cout<<"inserting: "<<key<<endl;
    RBNode * z=new RBNode;
    z->key=key;
    z->p=z->l=z->r=this->nil;
    if (this->root==this->nil){
        this->root=z;
        this->insertFix(z);
        return;
    }
    RBNode * p=this->root;
    while (true){
        if (key<p->key){
            if(p->l==this->nil) {
                z->p=p;
                p->l=z;
                break;
            }
            p=p->l;
            continue;
        }
        if(p->r==this->nil) {
            z->p=p;
            p->r=z;
            break;
        }
        p=p->r;
    }
    this->insertFix(z);
}

void RBTree::insertFix(RBNode * z){
    cout<<"insert fixing: "<<z->key<<endl;
    while (z->p->c==red){
        if(z->p==z->p->p->l){
            RBNode * u=z->p->p->r;
            //case 1
            if(u->c==red){
                z->p->p->c=red;
                z->p->c=black;
                u->c=black;
                z=z->p->p;
            }else{
                //case 2, will be converted to case 3
                if(z==z->p->r){
                    this->leftRotate(z->p);
                    z=z->l;
                }
                //case 3
                if(z==z->p->l){
                    this->rightRotate(z->p->p);
                    z->p->c=black;
                    z->p->r->c=red;
                }
            }
        }else{
            RBNode * u=z->p->p->l;
            //case 1
            if(u->c==red){
                z->p->p->c=red;
                z->p->c=black;
                u->c=black;
                z=z->p->p;
            }else{
                //case 2, will be converted to case 3
                if(z==z->p->l){
                    this->rightRotate(z->p);
                    z=z->r;
                }
                //case 3
                if(z==z->p->r){
                    this->leftRotate(z->p->p);
                    z->p->c=black;
                    z->p->l->c=red;
                }
            }
        }
    }
    if (z==this->root)
        z->c=black;
}

void RBTree::del(RBNode * node){
    cout<<"deleting: "<<node->key<<endl;
    RBNode * x;
    Color delColor;
    if(node->r!=this->nil && node->l!=this->nil){
        RBNode * successor=this->getSuccessor(node);
        node->key=successor->key;
        delColor=successor->c;
        this->transplant(successor,successor->r);
        x=successor->r;
    }else{
        delColor=node->c;
        if(node->l!=this->nil){
            this->transplant(node,node->l);
            x=node->l;
        }else if(node->r!=this->nil){
            this->transplant(node,node->r);
            x=node->r;
        }else{
            this->transplant(node,this->nil);
            x=this->nil;
        }
    }

    if (delColor==black)
        this->delFix(x);
}

void RBTree::delFix(RBNode * x){
    cout<<"delFixing: "<<x->key<<endl;
    while(x->c==black){ 
        if(x==x->p->l){
            RBNode * sib=x->p->r;
            //case 1
            if(sib->c==red){
                x->p->c=red;
                sib->c=black;
                this->leftRotate(x->p);
                sib=x->p->r;
            }
            //case 2
            if(sib->c==black){
                if(sib->l->c==black && sib->r->c==black){
                    sib->c=red;
                    x=x->p;
                    continue;
                }
                //case 3
                if(sib->r->c==black){
                    sib->l->c=black;
                    sib->c=red;
                    this->rightRotate(sib);
                    sib=sib->p;
                }
                //case 4
                if(sib->r->c==red){
                    Color oldColor=x->p->c;
                    x->p->c=black;
                    sib->c=oldColor;
                    sib->r->c=black;
                    this->leftRotate(x->p);
                    x=this->root;
                    break;
                }
            }
        }else{
            RBNode * sib=x->p->l;
            //case 1
            if(sib->c==red){
                x->p->c=red;
                sib->c=black;
                this->rightRotate(x->p);
                sib=x->p->l;
            }
            //case 2
            if(sib->c==black){
                if(sib->r->c==black && sib->l->c==black){
                    sib->c=red;
                    x=x->p;
                    continue;
                }
                //case 3
                if(sib->l->c==black){
                    sib->r->c=black;
                    sib->c=red;
                    this->leftRotate(sib);
                    sib=sib->p;
                }
                //case 4
                if(sib->l->c==red){
                    Color oldColor=x->p->c;
                    x->p->c=black;
                    sib->c=oldColor;
                    sib->l->c=black;
                    this->rightRotate(x->p);
                    x=this->root;
                    break;
                }
            }
        }
    }
    x->c=black;
}

int main(){
    RBTree tree;
    tree.insert(5);
    tree.prettyPrint();
    tree.insert(1);
    tree.prettyPrint();
    tree.insert(2);
    tree.prettyPrint();
    tree.insert(98);
    tree.prettyPrint();
    tree.insert(23);
    tree.prettyPrint();
    tree.insert(3);
    tree.prettyPrint();
    tree.del(tree.search(2));
    tree.prettyPrint();
    tree.insert(7);
    tree.prettyPrint();
    tree.insert(33);
    tree.insert(21);
    tree.insert(21);
    tree.insert(21);
    tree.insert(33);
    tree.insert(21);
    tree.insert(21);
    tree.insert(21);
    tree.insert(21);
    tree.insert(21);
    tree.insert(21);
    tree.insert(21);
    tree.insert(21);
    tree.insert(21);
    tree.insert(21);
    tree.insert(21);
    tree.insert(21);
    tree.insert(21);
    tree.prettyPrint();
    tree.del(tree.search(33));
    tree.prettyPrint();
    tree.del(tree.search(21));
    tree.prettyPrint();
    tree.del(tree.search(21));
    tree.prettyPrint();
    return 0;
}

