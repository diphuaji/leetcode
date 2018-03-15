#include<iostream>
#include<string>
#include<cstring>
#include<cstdlib>

using namespace std;

void  buildTree(int k[],float p[],float q[],int d,void * e1,void * w1,void * root1 ){
    float  (*e)[d+1][d+1]=(float (*)[d+1][d+1])e1;
    float (*w)[d+1][d+1]=(float (*)[d+1][d+1])w1;
    int (*root)[d][d]=(int (*)[d][d])root1;
    //init e, w
    for(int i=0;i<d+1;i++){
        (*e)[i][i]=(*w)[i][i]=q[i];
    }
    int iAdjust = -1;
    for(int l=1;l<d+1;l++){
        for(int i=1;i<=d-l+1;i++){
            int j=i+l-1;
            (*e)[i+iAdjust][j] = 1.0*0xffffffff;
            (*w)[i+iAdjust][j] = (*w)[i+iAdjust][j-1]+p[j-1]+q[j];
            //cout<<"w "<<i<<","<<j<<"="<<w[i][j];
            for(int r=i;r<=j;r++){
                float t=(*e)[i+iAdjust][r-1]+(*e)[r][j]+(*w)[i+iAdjust][j];
                if(t<(*e)[i+iAdjust][j]){
                    (*e)[i+iAdjust][j]=t;
                    (*root)[i+iAdjust][j-1]=r;
                }
            }
        }
    }
}

int main(){
    int k[] = {1,5,6,7,9};
    float p[] ={0.15,0.10,0.05,0.10,0.20};
    float q[] ={0.05,0.10,0.05,0.05,0.05,0.10};
    int d=sizeof(p)/sizeof(float);
    float e[d+1][d+1];
    float w[d+1][d+1];
    int root[d][d];
    buildTree(k,p,q,d,e,w,root);
    cout<<"w-----"<<endl;
    for(int i=0;i<d+1;i++){
        for(int j=0;j<d+1;j++){
            cout<<"\t"<<w[i][j];
        }
        cout<<endl;
    }
    cout<<"e-----"<<endl;
    for(int i=0;i<d+1;i++){
        for(int j=0;j<d+1;j++){
            cout<<"\t"<<e[i][j];
        }
        cout<<endl;
    }
    cout<<"root-----"<<endl;
    for(int i=0;i<d;i++){
        for(int j=0;j<d;j++){
            cout<<"\t"<<root[i][j];
        }
        cout<<endl;
    }
    return 0;
}
