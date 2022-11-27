#include<bits/stdc++.h>
using namespace std;
char answers_by_bot[105];
int count1=0;
class word
{
    public:
        string x;
        word();
        word(string a);
        void print() const
        {
            for(int i=0;i<x.size();i++)
               answers_by_bot[++count1]=x[i];
        }
        word operator * (word b);
        friend bool operator < (word a, word b)
        {
            for(int i=0;i<a.x.size();i++)
            if(a.x[i]<b.x[i]) return true;
                else if(a.x[i]>b.x[i]) return false;
            return false;
        }
        friend bool operator == (word a, word b)
        {
            if(a.x==b.x) return true;
            return false;
        }
        bool good(word a, word b) const;
        int get_number()
        {
            int digit,number=0,power=1;
            for(int i=0;i<x.size();i++)
            {
                if(x[i]=='G') digit=0;
                    else if(x[i]=='Y') digit=1;
                        else digit=2;
                number+=power*digit;
                power*=3; 
            }
            return number;
        }
};
word::word()
{
    x="";
}
word::word(string a)
{
    x=a;
}
word word::operator * (word b)
{
    word temp;
    string ans="BBBBB",good_word=x,check_word=b.x;
    for(int i=0; i<good_word.size(); i++)
        if(good_word[i]==check_word[i])
            ans[i]='G';
    for(int i=0;i<check_word.size();i++)
        if(ans[i]!='G')
        {
            for(int j=0;j<good_word.size();j++)
                if(check_word[i]==good_word[j])
                {
                    ans[i]='Y';
                    break;
                }
        }
    temp.x=ans;
    return temp;
}
bool word::good(word a, word b) const
{
    for(int i=0;i<5;i++)
    {
        switch(b.x[i])
        {
            case 'G':
            {
                if(x[i]!=a.x[i]) return 0;
                break;
            }
            case 'B':
            {
                for(int j=0;j<5;j++)
                    if(x[j]==a.x[i]) return 0;
                break;
            }
            default:
            {
                if(x[i]==a.x[i]) return 0;
                bool ok=0;
                for(int j=0;j<5;j++)
                    if(x[j]==a.x[i] && j!=i) ok=1;
                if(ok==0) return 0;
                break;
            }
        }
    }
    return 1;
}
vector<word>m,full_database;
void create_database()
{
    string path = __FILE__; //gets source code path, include file name
	path = path.substr(0, 1 + path.find_last_of('\\')); //removes file name
	path += "cuvinte_wordle.txt"; //adds input file to path
    ifstream file1;
    file1.open(path);
    string s;
    while(getline(file1,s))
    {
        word ins(s);
        m.push_back(ins);
        full_database.push_back(ins);
    }
    file1.close();
}
word chosen_word;