#include"player.cpp"
using namespace std;
string config="     ";
word currentword;
word savedword;
double ENTROPY,MAXENTROPY=0;
const double eps=0.e-14;
int NUMBER=0;
void add_hints(word verifiedword, string feedback, vector<char> &negru, vector<char> &galben, vector<pair<char,int>> &verde)
{
    for(int i=0;i<feedback.size();i++)
    {
        switch(feedback[i])
        {
            case 'Y':
            {
                int ok=0;
                for(int j=0;j<galben.size();j++)
                    if(galben[j]==verifiedword.x[i]) ok=1;
                if(ok==0) galben.push_back(verifiedword.x[i]);
                break;
            }
            case 'B':
            {
                int ok=0;
                for(int j=0;j<negru.size();j++)
                    if(negru[j]==verifiedword.x[i]) ok=1;
                if(ok==0) negru.push_back(verifiedword.x[i]);
                break;
            }
            default:
                verde.push_back(make_pair(verifiedword.x[i],i));
        }
    }
} 
void do_entropy()
{
    vector<char>blackcopy(black),yellowcopy(yellow);
    vector<pair<char,int>>greencopy(green);
    add_hints(currentword,config,black,yellow,green);
    map<word,bool>:: iterator it2 = m.begin();
    int count=0;
    for(;it2!=m.end();it2++)
        if((*it2).second==1) if((*it2).first.good()==1) count++;
    double P = double((1.0*count)/(1.0*m.size()));
    if(P!=0)
    {
    double log = double(log2(1/P));
    ENTROPY += P * log;
    }
    green.assign(greencopy.begin(),greencopy.end());
    yellow.assign(yellowcopy.begin(),yellowcopy.end());
    black.assign(blackcopy.begin(),blackcopy.end());
    /// Copy structures
    /// Modify original ones -- ai grija la asta
    /// Test for each element and obtain value for 1 configuration
}
void backtracking(int k)
{
    if(k==5) {do_entropy(); return;}
    config[k]='B'; backtracking(k+1);
    config[k]='G'; backtracking(k+1);
    config[k]='Y'; backtracking(k+1);
   // printf("%d\n",k);
    return;
}
void start_game_bot()
{
    map<word,bool>:: iterator it = m.begin(),it3=m.begin();
    advance(it3,20);
    for( ;it!=it3;it++)
    {
        currentword = (*it).first;
        ENTROPY = 0;
        config="     ";
        NUMBER=0;
        backtracking(0);
        if(ENTROPY-MAXENTROPY>eps)
        {
            MAXENTROPY=ENTROPY;
            savedword=currentword;
        }
        /// Obtain entropy level, save word if maximum case;
    }
    savedword.print();
    printf("%d: %lf\n",NUMBER,MAXENTROPY);
}