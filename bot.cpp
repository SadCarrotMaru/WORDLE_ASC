#include<bits/stdc++.h>
#include"player.cpp"
using namespace std;
string config="     ";
double do_entropy()
{
    /// Copy structures
    /// Modify original ones -- ai grija la asta
    /// Test for each element and obtain value for 1 configuration
}
void backtracking(int k)
{
    if(k==5) do_entropy();
    if(config[k]==' ') config[k]='B';
        else if (config[k]=='B') config[k]='G';
            else if(config[k]=='G') config[k]='Y';
                else return;
    backtracking(k+1);
}
void start_game_bot()
{
    map<word,bool>:: iterator it = m.begin();
    for( ;it!=m.end();it++)
    {
        backtracking(0);
        /// Obtain entropy level, save word if maximum case;
    }
}