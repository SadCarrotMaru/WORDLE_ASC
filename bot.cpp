#include"player.cpp"
using namespace std;
word currentword;
word savedword("TAREI");
double ENTROPY,MAXENTROPY=0,SUM=0;
const double eps=0.e-14;
int countg;
map<word,bool>vizitat;
void update_database()
{
    // TRANSMIT SAVEDWORD TO PY INTERFACE TO TEST IT
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
    int frecv[250] = {0};
    // B - > 1, Y -> 2, G -> 3- > 31311
    int count=0,number;
    for(auto &x: m)
    {
        word config;
        config = x * currentword;
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
}
void chosen_word_by_bot(word choice)
{
    vizitat.insert(make_pair(savedword,1));
    update_database();
    countg++;
    choice.print();
    af << ", ";
    // TRANSMIT WORD TO BOT

}
void start_game_bot()
{
    //debug();
    vizitat.clear();
    savedword.x = "TAREI";
    countg = 0;
    chosen_word.print();
    af << "  -->  ";
    chosen_word_by_bot(savedword);
    while(m.size())
    {
        MAXENTROPY=-1;
        bool ok = false;
        if(m.size()==1)
            {chosen_word_by_bot(m.front()); break;}
        else
        {
            for(auto &y : full_database)
            {
                if(vizitat.find(y)==vizitat.end())
                {
                    currentword = y;
                    ENTROPY = 0;
                    do_entropy();
                    if(ENTROPY-MAXENTROPY>eps)
                    {
                        MAXENTROPY=ENTROPY;
                        savedword=currentword;
                        ok = true;
                    }
                }
            }
            if(ok==true) chosen_word_by_bot(savedword);
        }
    }
    af << countg << '\n';
    //printf("%d \n",countg);
    SUM += countg;
    //af.close();
}