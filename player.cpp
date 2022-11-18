#include"structures.cpp"
using namespace std;
word user_input;
word good("GGGGG");
void get_user_input()
{
    printf("Enter your guess:\n");
    string s;
    while(1)
    {
        getline(cin,s);
        if(s.size()==5)
        {
            word input(s);
            if(find(input))
            {
                user_input=input;
                break;
            }
        }
        printf("\nInvalid word! Try again:\n");
    }
}
void start_game_player()
{
    while(1)
    {
        get_user_input();
        word feedback;
        feedback = chosen_word + user_input;
        feedback.print();
        if(feedback == good)
        {
            printf("YOU WON!\n");
            break;
        }
    }
}
