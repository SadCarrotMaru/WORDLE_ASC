#include<bits/stdc++.h>
using namespace std;
int main()
{
    string path2, path = __FILE__; //gets source code path, include file name
	path = path.substr(0, 1 + path.find_last_of('\\')); //removes file name
    path += "test.txt";
    freopen(path.c_str(),"w",stdout);
    cout<<"TE ROG";
}