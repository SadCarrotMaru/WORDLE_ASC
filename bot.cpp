#include"player.cpp"
using namespace std;
word currentword;
word savedword("TAREI");
double ENTROPY,MAXENTROPY=0;
const double eps=0.e-14;
void update_database()
{
    word feedback;
    feedback = savedword * chosen_word;
    vector<word>m2;
    m2.clear();
    for(auto &x : m)
    {
        if(x.good(savedword,feedback))
            m2.push_back(x);
    }
    m.clear();
    m=m2;
}
// ABACA   ->  ATARE  -> GBGBB
void do_entropy()
{
    int frecv[250] = {0};
    // B - > 1, Y -> 2, G -> 3- > 31311
    int count=0,number;
    for(auto &x: m)
    {
        word config;
        config = currentword * x;
        number = config.get_number();
        frecv[number]++;
    }
    double P=1;
    for(int i=0;i<=243;i++)
    {
        if(frecv[i])
        {
            P = frecv[i] / (1.0*m.size());
            double logP = double(log2(1/P));
            ENTROPY += P * logP;
        }
    }
    /*
    double P = double((1.0*count)/(1.0*m.size()));
    if(P!=0)
    {
    double logP = double(log2(1/P));
    ENTROPY += P * logP;
    }
    */
}
/*
void backtracking(int k)
{
    if(k==5) {do_entropy(); return;}
    config[k]='B'; backtracking(k+1);
    config[k]='G'; backtracking(k+1);
    config[k]='Y'; backtracking(k+1);
    return;
}
*/
void chosen_word_by_bot(word choice)
{
    update_database();
    printf("Entropy: %lf found with the word:\n",MAXENTROPY);
    choice.print();
    /// ANIMATION PYTHON

}
void debug()
{
    word a("ABATA");
    word b("MAMTE");
    word c("BYBBB");
    printf("%d ",a.good(b,c));
}
void start_game_bot()
{
    debug();
    update_database();
    while(m.size())
    {
        MAXENTROPY=0;
        printf("%d  ",m.size());
        for(auto currentword : m)
        {
            ENTROPY = 0;
            do_entropy();
            if(ENTROPY-MAXENTROPY>eps)
            {
                MAXENTROPY=ENTROPY;
                savedword=currentword;
            }
        }
        if(savedword==chosen_word)
        {
            printf("YOU WON\n");        
        }   
        chosen_word_by_bot(savedword);
    }
}