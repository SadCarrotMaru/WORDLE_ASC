#include<bits/stdc++.h>
using namespace std;
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
        bool good(word a, word b) const;
        int get_number()
        {
            int digit,number,power=1;
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
                bool ok=0;
                for(int j=0;j<5;j++)
                    if(x[j]==a.x[i]) ok=1;
                if(ok==0) return 0;
                break;
            }
        }
    }
    return 1;
}
vector<word>m;
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
    }
    printf("%d\n",m.size());
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
    chosen_word = m[pos];
}
bool find(word a)
{
    int st=0,dr=m.size()-1;
    while(st<=dr)
    {
        int med=(st+dr)>>1;
        if(m[med]==a) return 1;
            else if(m[med].x<a.x) st=med+1;
                else dr=med-1;
    }
    return 0;
}