#include<iostream>
#include<string>
#include<cstring>
#include<cstdlib>

using namespace std;

float *  buildTree(int k[],float p[],float q[],int d){
    float e[d+1][d+1];
    float w[d+1][d+1];
    int root[d][d];
    //init e, w
    for(int i=0;i<d+1;i++){
        e[i][i]=w[i][i]=q[i];
    }
    for(int l=1;l<d-1;l++){
        for(int i=0;i<d-l+1;i++){
            int j=i+l;
            e[i][j] = 1.0*0xffffffff;
            w[i][j] = w[i][j-1]+p[j-1]+q[j];
            for(int r=i+1;r<=j;r++){
                float t=e[i][r-1]+e[r+1][j]+w[i][j];
                if(t<e[i][j]){
                    e[i][j]=t;
                    root[i][j]=r;
                }
            }
        }
    }
    for(int i=0;i<d+1;i++){
        for(int j=0;j<d+1;j++){
            cout<<"\t"<<w[i][j];
        }
        cout<<endl;
    }
    for(int i=0;i<d;i++){
        for(int j=0;j<d;j++){
            cout<<"\t"<<root[i][j];
        }
        cout<<endl;
    }
    void * rst=malloc(sizeof(root));
    memcpy(rst,root,sizeof(root));
    return (float *)rst;
}

int main(){
    int k[] = {1,5,6,7,9};
    float p[] ={0.15,0.10,0.05,0.10,0.20};
    float q[] ={0.05,0.10,0.05,0.05,0.05,0.10};
    int d=sizeof(p)/sizeof(float);
    float * root=buildTree(k,p,q,d);
    for(int i=0;i<d;i++){
        for(int j=i+1;j<d;j++){
            cout<<"|"<<*(root+i*d+j);
        }
        cout<<endl;
    }
    return 0;
}
