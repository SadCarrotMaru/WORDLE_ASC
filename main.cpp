#include"bot.cpp"
using namespace std;
int main()
{
    create_database();
    get_word();
    chosen_word.print();
    printf("\nCHOOSE GAMEMODE:\nPLAYER: 1\nPC: 2\n");
    int GAMEMODE;
    while(scanf("%d",&GAMEMODE))
    {
        if(GAMEMODE!=1&&GAMEMODE!=2) printf("PLEASE ENTER VALID INPUT! :D\n");
            else break;
    }
    getchar();
    switch (GAMEMODE)
    {
        case 1: 
        {
            start_game_player();
            break;
        }
        case 2: 
        {
            start_game_bot();
            break;
        }
        default: printf("FATAL ERROR OCCURED... WE ARE SORRY");
    }   
    return 0;
}
