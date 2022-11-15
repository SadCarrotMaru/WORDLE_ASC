#include<bits/stdc++.h>
using namespace std;
vector<char>black,yellow;
vector<pair<char,int>>green;
class word
{
    public:
        string x;
        word();
        word(string a);
        void print() const
        {
            for(int i=0;i<x.size();i++)
                printf("%c",x[i]);
            printf("\n");
        }
        word operator + (word b);
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
        bool good() const;
};
word::word()
{
    x="";
}
word::word(string a)
{
    x=a;
}
word word::operator + (word b)
{
    word temp;
    map<int,int>m_good,m_check;
    string ans="BBBBB",good_word=x,check_word=b.x;
    for(int i=0; i<good_word.size(); i++)
        if(good_word[i]==check_word[i])
        {
            ans[i]='G';
            good_word[i]=check_word[i]='0';
        }
    for(int i=0; i<good_word.size(); i++)
        if(good_word[i]!='0')
            m_good[good_word[i]]++;
    for(int i=0; i<check_word.size(); i++)
        if(check_word[i]!='0')
            m_check[check_word[i]]++;
    for(int i=0; i<good_word.size(); i++)
        if(good_word[i]!='0' && m_good[good_word[i]]>0)
            for(int j=0; j<check_word.size(); j++)
                if(ans[j]=='B' && m_good[good_word[i]]>0 && m_check[check_word[j]]>0)
                    if(good_word[i]==check_word[j])
                    {
                        ans[j]='Y';
                        m_good[good_word[i]]--;
                        m_check[check_word[j]]--;
                    }
    temp.x=ans;
    return temp;
}
word word::operator * (word b)
{
    word temp;
    map<int,int>m_good,m_check;
    string ans="BBBBB",good_word=x,check_word=b.x;
    for(int i=0; i<good_word.size(); i++)
        if(good_word[i]==check_word[i])
        {
            ans[i]='G';
            good_word[i]=check_word[i]='0';
        }
    for(int i=0;i<check_word.size();i++)
        if(check_word[i]!='0')
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
bool word::good() const
{
    string check_word=x;
    for(int i=0; i<green.size(); i++)
        if(check_word[green[i].second]!=green[i].first)
            return 0;
        else
            check_word[green[i].second]='0';
    for(int i=0; i<black.size(); i++)
        for(int j=0; j<check_word.size(); j++)
            if(black[i]==check_word[j])
                return 0;
    for(int i=0; i<yellow.size(); i++)
    {
        int ok=0;
        for(int j=0; j<check_word.size(); j++)
            if(yellow[i]==check_word[j])
            {
                ok=1;
                break;                
            }
        if(ok==0) return 0;
    }
    return 1;
}
map<word,bool>m;
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
        m.insert(pair<word,bool>(ins,1));
    }
    file1.close();
}
word chosen_word;
int random()
{
    random_device rd;
    mt19937::result_type seed = rd() ^ (
            (mt19937::result_type)
            chrono::duration_cast<chrono::seconds>(
                chrono::system_clock::now().time_since_epoch()
                ).count() +
            (mt19937::result_type)
            chrono::duration_cast<chrono::microseconds>(
                chrono::high_resolution_clock::now().time_since_epoch()
                ).count() );

    std::mt19937 gen(seed);
    std::uniform_int_distribution<unsigned> distrib(0, m.size());
    return distrib(gen);
}
void get_word()
{
    map<word,bool>::iterator it;
    int pos = random();
    it = m.begin();
    advance(it, pos);
    (*it) . second = 0;
    chosen_word = (*it).first;
}
