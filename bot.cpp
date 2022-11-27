#include"structures.cpp"
#include<fcntl.h>
#include<stdlib.h>
#include<unistd.h>
using namespace std;
word currentword;
word savedword("TAREI");
double ENTROPY,MAXENTROPY=0;
bool doit=1;
map<word,bool>vizitat;
vector<word>answers;
void update_database()
{
    word feedback;
    feedback = chosen_word * savedword;
    vector<word>m2;
    m2.clear();
    for(auto &x : m)
    {
        if(x.good(savedword,feedback) && !(x==savedword))
            m2.push_back(x);
    }
    m.clear();
    m=m2;
}
void do_entropy()
{
    int frecv[250];
    for(int i=0;i<=243;i++)
        frecv[i]=0;
    int count=0,number;
    for(auto &x: m)
    {
        word config;
        config = x * currentword;
        number = config.get_number();
        frecv[number]++;
    }
    double P=1;
    ENTROPY=0;
    for(int i=0;i<=243;i++)
    {
        if(frecv[i])
        {
            P = frecv[i] / (double)m.size();
            double logP = -log2(P);
            ENTROPY += P * logP;
        }
    }
}
void chosen_word_by_bot()
{
    vizitat.insert(make_pair(savedword,1));
    if(doit==0) savedword.print();
    update_database();
}
void start_game_bot()
{
    m = full_database;
    vizitat.clear();
    if(answers.size()>0)
    {
        for(int i=0;i<answers.size();i++)
        {
            savedword=answers[i];
            chosen_word_by_bot();
        }
        doit = 0;
    }
        else
        {
            doit = 0;
            savedword.x = "TAREI";
            chosen_word_by_bot();
        }
    while(m.size())
    {
        bool ok = false;
        ENTROPY = 0;
        currentword = m.front();
        savedword = m.front();
        do_entropy();
        MAXENTROPY=ENTROPY;
        for(auto &y : full_database)
        {
            if(vizitat.find(y)==vizitat.end())
            {
                currentword = y;
                do_entropy();
                if(ENTROPY>MAXENTROPY)
                {
                   MAXENTROPY=ENTROPY;
                   savedword=currentword;
                }
              }
        }
        chosen_word_by_bot();
    }
}
int main()
{
    create_database();
    string path2, path = __FILE__; //gets source code path, include file name
	path = path.substr(0, 1 + path.find_last_of('\\')); //removes file name
    path2 = path + "/tmp/file2.txt";
    path += "/tmp/file1.txt";
    string s;
    freopen(path.c_str(),"r",stdin);
    freopen(path2.c_str(),"w",stdout);
    getline(cin,s);
    word aj;
    chosen_word.x="";
    for(int i=0;i<s.size();i++)
    {
        aj.x +=s[i];
        if(aj.x.size()==5)
        {
            if(chosen_word.x=="") chosen_word=aj;
                else answers.push_back(aj);
            aj.x="";
        }   
    }
    start_game_bot();
    for(int i=1;i<=count1;i++)
        cout<<answers_by_bot[i];
    // Make vector
    return 0;
}