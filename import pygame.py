import pygame       # asta il stiti
import pyautogui
import sys          # ca sa inchidem procesul
import random       # sa genereze cuvant random
import os
#from words import * # lista lui de cuvinte, o modificam noi cand combinam
pygame.init()       # initializezi aplicatia
# Constants
WORDS = []
WIDTH, HEIGHT = 637, 750       # dimensiunile aplicatiei 

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))        # seteaza display-ul pentru aplicatie si incarca fundalul cu sloturile de cuvinte
BACKGROUND = pygame.image.load("1.jpg")     # ( il aveti in fisier )
BACKGROUND_RECT = BACKGROUND.get_rect(center=(317, 250))
ICON = pygame.image.load("Icon.png")       # iconita aplicatiei ( tot in fisier e)

pygame.display.set_caption("Wordle - Sad Carrot Team")  # cum se numeste aplicatia
pygame.display.set_icon(ICON)                # seteaza iconita

# Culorile, pretty self-explanatory
GREEN = "#6aaa64"
YELLOW = "#c9b458"
GREY = "#787c7e"
OUTLINE = "#3f1b40"
FILLED_OUTLINE = "#000000"



# ruleaza pt cuvantul coder prima data ( facut asa pt teste)
CORRECT_WORD = "VERDE"

# literele afisate pe tastatura
ALPHABET = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

#Fontul folosit la afisarea literelor
GUESSED_LETTER_FONT = pygame.font.Font(None, 50)
AVAILABLE_LETTER_FONT = pygame.font.Font(None, 25)

#pentru a desena pe ecran, cautati .blit si .fill de la pygame pt a intelege mai bine daca vreti
SCREEN.fill("white")
SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
pygame.display.update()

# spatiul dintre litere dupa ce dau display la una din ele + dimensiunea la care ii dau display
LETTER_X_SPACING = 85
LETTER_Y_SPACING = 11
LETTER_SIZE = 73

# Global variables

#cate cuvinte a incercat utilizatorul
guesses_count = 0

# guesses is a 2D list that will store guesses. A guess will be a list of letters.
# The list will be iterated through and each letter in each guess will be drawn on the screen.
guesses = [[] for _ in range(6)] 
all_guesses = []
start_ind_scroll = 0
#cuvantul pe care il tasteaza utilizatorul
current_guess = []
current_guess_string = ""
# x ul dupa care porneste display ul primului guess
current_letter_bg_x = 110

# Indicators is a list storing all the Indicator object. An indicator is that button thing with all the letters you see.
indicators = []

game_result = ""

# Asta e clasa pentru o litera, folosesti o clasa ca sa iti fie mai usor sa lucrezi cu ele si sa le poti generaliza
class Letter:
    def __init__(self, text, bg_position):
        # Initializes all the variables, including text, color, position, size, etc.
        self.bg_color = "#3f1b40"        # culoare fundal
        self.text_color = "white"      # culoare litera
        self.bg_position = bg_position    # coordonate caseta
        self.bg_x = bg_position[0]        # sa le pot accesa pentru control cu mouse ul
        self.bg_y = bg_position[1]        #                 --.--
        self.bg_rect = (bg_position[0], self.bg_y, LETTER_SIZE, LETTER_SIZE)
        self.text = text
        self.text_position = (self.bg_x+36, self.bg_y+34)
        self.text_surface = GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.text_position)

    def draw(self):
        # Puts the letter and text on the screen at the desired positions.
        pygame.draw.rect(SCREEN, self.bg_color, self.bg_rect)
        if self.bg_color == "#3f1b40":
            pygame.draw.rect(SCREEN, FILLED_OUTLINE, self.bg_rect, 3)
        self.text_surface = GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
        SCREEN.blit(self.text_surface, self.text_rect)
        pygame.display.update()

    def delete(self):
        # Fills the letter's spot with the default square, emptying it.
        pygame.draw.rect(SCREEN, "#3f1b40", self.bg_rect)
        pygame.draw.rect(SCREEN, OUTLINE, self.bg_rect, 3)
        pygame.display.update()

class Indicator:
    def __init__(self, x, y, letter, lengthx, lengthy):
        # Initializes variables such as color, size, position, and letter.
        self.x = x+10
        self.y = y+10
        self.xx = self.x + lengthx
        self.yy = self.y + lengthy
        self.text = letter
        self.rect = (self.x, self.y, lengthx, lengthy)
        self.bg_color = OUTLINE

    def draw(self, allignx = 27, alligny = 30):
        # Puts the indicator and its text on the screen at the desired position.
        pygame.draw.rect(SCREEN, self.bg_color, self.rect)
        self.text_surface = AVAILABLE_LETTER_FONT.render(self.text, True, "white")
        self.text_rect = self.text_surface.get_rect(center=(self.x+allignx, self.y+alligny))
        SCREEN.blit(self.text_surface, self.text_rect)
        pygame.display.update()

# Drawing the indicators on the screen.

indicator_x, indicator_y = 10, 500
default_indicator_lengthx, default_indicator_lengthy = 55, 55
for i in range(3):
    for letter in ALPHABET[i]:
        new_indicator = Indicator(indicator_x, indicator_y, letter, default_indicator_lengthx, default_indicator_lengthy)
        indicators.append(new_indicator)
        new_indicator.draw()
        indicator_x += 60
    indicator_y += 75
    if i == 0:
        indicator_x = 38
    elif i == 1:
        indicator_x = 98

def check_guess(guess_to_check):
    # Goes through each letter and checks if it should be green, yellow, or grey.
    global current_guess, current_guess_string, guesses_count, current_letter_bg_x, game_result, start_ind_scroll
    game_decided = False
    for i in range(5):
        lowercase_letter = guess_to_check[i].text.upper()
        if lowercase_letter in CORRECT_WORD:
            if lowercase_letter == CORRECT_WORD[i]:
                guess_to_check[i].bg_color = GREEN
                for indicator in indicators:
                    if indicator.text == lowercase_letter.upper():
                        indicator.bg_color = GREEN
                        indicator.draw()
                guess_to_check[i].text_color = "white"
                if not game_decided:
                    game_result = "W"
            else:
                guess_to_check[i].bg_color = YELLOW
                for indicator in indicators:
                    if indicator.text == lowercase_letter.upper() and indicator.bg_color != GREEN:
                        indicator.bg_color = YELLOW
                        indicator.draw()
                guess_to_check[i].text_color = "white"
                game_result = ""
                game_decided = True
        else:
            guess_to_check[i].bg_color = GREY
            for indicator in indicators:
                if indicator.text == lowercase_letter.upper():
                    indicator.bg_color = GREY
                    indicator.draw()
            guess_to_check[i].text_color = "white"
            game_result = ""
            game_decided = True
        guess_to_check[i].draw()
        pygame.display.update()
    
    guesses_count += 1
    all_guesses.append([])
    for letter in current_guess:
        new_letter = Letter(letter.text, letter.bg_position)
        new_letter.bg_color = letter.bg_color
        all_guesses[-1].append(new_letter)
    current_guess = []
    current_guess_string = ""
    current_letter_bg_x = 110
    if guesses_count == 6:
        start_ind_scroll +=1
        list_update()

def play_again():
    # Puts the play again text on the screen.
    pygame.draw.rect(SCREEN, "#943CB5", (0, 600, 1000, 600))
    play_again_font = pygame.font.Font(None, 40)
    play_again_text = play_again_font.render("Press ENTER to Play Again!", True, "white")
    play_again_rect = play_again_text.get_rect(center=(WIDTH/2, 700))
    word_was_text = play_again_font.render(f"You won! The word was {CORRECT_WORD}!", True, "white")
    word_was_rect = word_was_text.get_rect(center=(WIDTH/2, 650))
    SCREEN.blit(word_was_text, word_was_rect)
    SCREEN.blit(play_again_text, play_again_rect)
    pygame.display.update()

def reset():
    # Resets all global variables to their default states.
    global guesses_count, CORRECT_WORD, guesses, current_guess, current_guess_string, game_result, current_letter_bg_x
    SCREEN.fill("white")
    SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
    guesses_count = 0
    CORRECT_WORD = random.choice(WORDS)
    guesses = [[] for _ in range(6)] 
    current_guess = []
    current_guess_string = ""
    game_result = ""
    pygame.display.update()
    current_letter_bg_x = 110
    for indicator in indicators:
        if indicator.text == "ENTER": break
        indicator.bg_color = OUTLINE
        indicator.draw()
    indicator_enter = Indicator(10,650,"ENTER",83,55)
    indicator_delete = Indicator(518,650,"DEL",83,55)
    indicator_enter.draw(41)
    indicator_delete.draw(41)
    indicator_button_up = Indicator(530,1,"^",70,70)
    indicator_button_down = Indicator(530,406,"v",70,70)
    indicator_button_up.draw(35,35)
    indicator_button_down.draw(35,35)
    

def is_inside(ind, pos):
    if pos[0]>=ind.x and pos[0]<=(ind.xx) and pos[1]>=ind.y and pos[1]<=(ind.yy):
        return True
    return False

def create_new_letter(letter):
    # Creates a new letter and adds it to the guess.
    global current_guess_string, current_letter_bg_x
    current_guess_string += letter
    new_letter = Letter(letter, (current_letter_bg_x, guesses_count*81+LETTER_Y_SPACING))
    current_letter_bg_x += LETTER_X_SPACING
    guesses[guesses_count].append(new_letter)
    current_guess.append(new_letter)
    #for guess in guesses:
    for letter in current_guess:
        letter.draw()


def delete_letter():
    # Deletes the last letter from the guess.
    global current_guess_string, current_letter_bg_x
    guesses[guesses_count][-1].delete()
    guesses[guesses_count].pop()
    current_guess_string = current_guess_string[:-1]
    current_guess.pop()
    current_letter_bg_x -= LETTER_X_SPACING

def list_update():
   global guesses_count, start_ind_scroll
   for guess in guesses:
        for letter in guess:
            letter.delete()
   for i in range(6):
        if i == 5 and start_ind_scroll == len(all_guesses) - 5: 
            break
        for j in range(5):
            guesses[i][j].text =  all_guesses[i+start_ind_scroll][j].text
            guesses[i][j].bg_color = all_guesses[i+start_ind_scroll][j].bg_color
            guesses[i][j].text_surface = GUESSED_LETTER_FONT.render(guesses[i][j].text, True, guesses[i][j].text_color)
            guesses[i][j].text_rect = guesses[i][j].text_surface.get_rect(center=guesses[i][j].text_position)
   guesses_count = 5
   for i in range(6):
        if i==5  and start_ind_scroll == len(all_guesses) -5: 
            break
        for j in range(5):
            guesses[i][j].draw()

def create_database():
    with open('cuvinte_wordle.txt') as openfileobject:
        for line in openfileobject:
            WORDS.append(line.rstrip(line[-1]))

def init_game():
    indicator_button_up = Indicator(530,1,"^",70,70)
    indicator_button_down = Indicator(530,406,"v",70,70)
    indicator_button_up.draw(35,35)
    indicator_button_down.draw(35,35)
    indicator_enter = Indicator(10,650,"ENTER",83,55)
    indicator_delete = Indicator(518,650,"DEL",83,55)
    indicator_robot = Indicator(530,205,"ROB",70,70)
    indicators.append(indicator_robot)
    robot_image = pygame.image.load("robot.jpg")
    SCREEN.blit(robot_image, (540,215))
    indicator_enter.draw(41)
    indicator_delete.draw(41)
    indicators.append(indicator_enter)
    indicators.append(indicator_delete)
    indicators.append(indicator_button_up)
    indicators.append(indicator_button_down)
    create_database()

# SERVER

def robot():
    directory = os.getcwd()
    directory += "\\tmp"
    file  = "file1.txt"
    file2 = "file2.txt"
    with open(os.path.join(directory, file), 'w') as fp:
        fp.write("ABACA")
    with open(os.path.join(directory, file2), 'r') as fp:
        line = fp.readline().strip()
        for ch in line:
            create_new_letter(ch)
            if len(current_guess_string) == 5: check_guess(current_guess)
    #execute_cpp
    os.system("procesu.exe")
    print("a intrat")
    



init_game()
while True:
    if game_result != "":
        play_again()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if game_result != "":
                    reset()
                else:
                    if len(current_guess_string) == 5 and current_guess_string in WORDS:
                        check_guess(current_guess)
            elif event.key == pygame.K_BACKSPACE:
                if len(current_guess_string) > 0:
                    delete_letter()
            elif event.key == pygame.K_SPACE:
                pyautogui.moveTo(100, 100, duration = 2)
            elif event.key == pygame.K_UP:
                if start_ind_scroll !=0:
                        start_ind_scroll = start_ind_scroll - 1
                        list_update()
            elif event.key == pygame.K_DOWN:
                if start_ind_scroll != len(all_guesses)-5 and len(all_guesses)>5:
                        start_ind_scroll = start_ind_scroll + 1
                        list_update()
            else:
                key_pressed = event.unicode.upper()
                if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                    if len(current_guess_string) < 5:
                        create_new_letter(key_pressed)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            indicator_found = [l for l in indicators if is_inside(l,pos)==True]
            if(len(indicator_found)!=0):
                text = indicator_found[0].text
                if text == "DEL":
                    if len(current_guess_string) > 0:
                        delete_letter()
                elif text == "ENTER":
                    if len(current_guess_string) == 5 and current_guess_string in WORDS:
                        check_guess(current_guess)
                elif text == "^":
                    if start_ind_scroll !=0:
                        start_ind_scroll = start_ind_scroll - 1
                        list_update()
                elif text == "v":
                    if start_ind_scroll != len(all_guesses)-5 and len(all_guesses)>5:
                        start_ind_scroll = start_ind_scroll + 1
                        list_update()
                elif text == "ROB":
                    robot()
                else:
                    if len(current_guess_string) < 5:
                        create_new_letter(text)
