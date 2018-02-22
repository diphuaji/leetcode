#include<iostream>
#include<memory>
#include<vector>
#include<string>
#include<fstream>
#include<sstream>
#include<stack>
#include<queue>
using namespace std;

enum Color{gray,white,black};
enum SectionStatus{null,inVertices,inEdges};

class Vertex{
    public:
        int id;
        Color c;
        vector<Vertex*> adjList;
        Vertex * p;
        int dt;
        int ft;
        int d;
};

class Graph{
    public:
        Graph(const string &);
        vector<Vertex> vList;
        void bfs(Vertex &);
        void dfs();
        string trim(const string &);
        vector<string> tokenize(const string &,char);
        void reset();
        bool isDirected=false;
};

vector<string> Graph::tokenize(const string & s,char delimiter=' '){
    string token;
    istringstream strm(s);
    vector<string> tokens;
    while(!strm.eof()){
        getline(strm,token, delimiter);
        if(token.size())
            tokens.push_back(this->trim(token));
    }
    return tokens;
}

Graph::Graph(const string & fname){
    ifstream infile(fname);
    string s;
    SectionStatus status=null;
    int vCount=0;
    while(!infile.eof()){
        getline(infile,s);
        if(s.find("*Vertices")!=string::npos){
            if(status==inVertices){
                cerr<<"vertices section duplicated!"<<endl;
                exit(1);
            }
            status=inVertices;
            continue;
        }
        if(s.find("*Edges")!=string::npos||s.find("*Arcs")!=string::npos){
            if(status==inEdges){
                cerr<<"edges section duplicated!"<<endl;
                exit(1);
            }
            if(s.find("*Arcs")!=string::npos) this->isDirected=true;
            status=inEdges;
            continue;
        }
        if(status==inVertices){
            Vertex v;
            v.id=++vCount;
            this->vList.push_back(v);
        }
        if(status==inEdges){
            if(this->trim(s).size()){
                vector<string> tokens=this->tokenize(s);
                cout<<tokens[0]<<":"<<tokens[1]<<"-"<<tokens[2]<<endl;
                this->vList[stoi(tokens[0])-1].adjList.push_back(&(this->vList[stoi(tokens[1])-1]));
                if(!this->isDirected){
                    this->vList[stoi(tokens[1])-1].adjList.push_back(&(this->vList[stoi(tokens[0])-1]));
                }
            }
        }
    }
}

void Graph::reset(){
    for(int i=0;i<this->vList.size();i++){
        Vertex & v=this->vList[i];
        v.c=white;
        v.p=NULL;
        v.d=0xffffffff;
        v.dt=0xffffffff;
        v.ft=0xffffffff;
    }
}

void Graph::bfs(Vertex & s){
    this->reset();
    s.c=gray;
    s.d=0;
    queue<Vertex *> grayQ;
    grayQ.push(&s);
    while(!grayQ.empty()){
        Vertex * v=grayQ.front();
        for (int i=0;i<v->adjList.size();i++){
            if(v->adjList[i]->c!=white) continue;
            v->adjList[i]->c=gray;
            v->adjList[i]->p=v;
            v->adjList[i]->d=v->d+1;
            grayQ.push(v->adjList[i]);
        }
        v->c=black;
        cout<<v->id<<" from s: "<<v->d<<endl;
        grayQ.pop();
    }
}

void Graph::dfs(){
    this->reset();
    int time=0;
    for(int i=0;i<this->vList.size();i++){
        Vertex * v=&(this->vList[i]);
        if(v->c!=white)
            continue;
        stack<Vertex *> vStack;
        stack<int> cntStack;
        v->c=gray;
        v->dt=++time;
        vStack.push(v);
        cntStack.push(0);
        while (!vStack.empty()){
            int cnt=cntStack.top();
            cntStack.pop();
            v=vStack.top();
            if(cnt==v->adjList.size()){
                v->c=black;
                v->ft=++time;
                vStack.pop();
                cout<<"id: "<<v->id<<endl;
                cout<<"dt: "<<v->dt<<endl;
                cout<<"ft: "<<v->ft<<endl;
                //cntStack.pop();
                continue;
            }
            Vertex * next=v->adjList[cnt++];
            //cout<<"next: "<<next->id<<endl;
            cntStack.push(cnt);
            if(next->c!=white)
                continue;
            next->dt=++time;
            next->p=v;
            next->c=gray;
            //cout<<"pushing: "<<next->id<<endl;
            vStack.push(next);
            cntStack.push(0);
        }
    }
}


string Graph::trim(const string & s){
    int start=0;
    int end=s.size()-1;
    for(;start<s.size();start++){
        if(!isspace(s[start]))
            break;
    }
    for(;end>start;end--){
        if(!isspace(s[end]))
            break;
    }    
    return s.substr(start,end-start+1);
}

void testBfs(string fname){
    cout<<"----Testing BFS----"<<endl;
    Graph graph(fname);
    //cout<<"v:"<<graph.vList.size()<<endl;
    cout<<"adjList size: "<<graph.vList[0].adjList.size()<<endl;
    graph.bfs(graph.vList[3]);
    
}

void testDfs(string fname){
    cout<<"----Testing DFS----"<<endl;
    Graph graph(fname);
    graph.dfs();
}


int main(){
    //testBfs("bfs_test.txt");
    testDfs("5.net");
    return 0;
}
