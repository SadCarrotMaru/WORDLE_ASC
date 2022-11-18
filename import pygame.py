import pygame
import sys
import random
from words import *
pygame.init()
# Constants
WIDTH, HEIGHT = 637, 750

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = pygame.image.load("Starting_Tiles.png")
BACKGROUND_RECT = BACKGROUND.get_rect(center=(317, 250))
ICON = pygame.image.load("Icon.png")

pygame.display.set_caption("Wordle - Sad Carrot Team")
pygame.display.set_icon(ICON)

GREEN = "#6aaa64"
YELLOW = "#c9b458"
GREY = "#787c7e"
OUTLINE = "#d3d6da"
FILLED_OUTLINE = "#878a8c"

CORRECT_WORD = "coder"

ALPHABET = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

GUESSED_LETTER_FONT = pygame.font.Font("FreeSansBold.otf", 50)
AVAILABLE_LETTER_FONT = pygame.font.Font("FreeSansBold.otf", 25)

SCREEN.fill("white")
SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
pygame.display.update()

LETTER_X_SPACING = 85
LETTER_Y_SPACING = 12
LETTER_SIZE = 72

# Global variables

guesses_count = 0

# guesses is a 2D list that will store guesses. A guess will be a list of letters.
# The list will be iterated through and each letter in each guess will be drawn on the screen.
guesses = [[]] * 6

current_guess = []
current_guess_string = ""
current_letter_bg_x = 110

# Indicators is a list storing all the Indicator object. An indicator is that button thing with all the letters you see.
indicators = []

game_result = ""

class Letter:
    def __init__(self, text, bg_position):
        # Initializes all the variables, including text, color, position, size, etc.
        self.bg_color = "white"
        self.text_color = "black"
        self.bg_position = bg_position
        self.bg_x = bg_position[0]
        self.bg_y = bg_position[1]
        self.bg_rect = (bg_position[0], self.bg_y, LETTER_SIZE, LETTER_SIZE)
        self.text = text
        self.text_position = (self.bg_x+36, self.bg_position[1]+34)
        self.text_surface = GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.text_position)

    def draw(self):
        # Puts the letter and text on the screen at the desired positions.
        pygame.draw.rect(SCREEN, self.bg_color, self.bg_rect)
        if self.bg_color == "white":
            pygame.draw.rect(SCREEN, FILLED_OUTLINE, self.bg_rect, 3)
        self.text_surface = GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
        SCREEN.blit(self.text_surface, self.text_rect)
        pygame.display.update()

    def delete(self):
        # Fills the letter's spot with the default square, emptying it.
        pygame.draw.rect(SCREEN, "white", self.bg_rect)
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

    def draw(self):
        # Puts the indicator and its text on the screen at the desired position.
        pygame.draw.rect(SCREEN, self.bg_color, self.rect)
        self.text_surface = AVAILABLE_LETTER_FONT.render(self.text, True, "white")
        self.text_rect = self.text_surface.get_rect(center=(self.x+27, self.y+30))
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
    global current_guess, current_guess_string, guesses_count, current_letter_bg_x, game_result
    game_decided = False
    for i in range(5):
        lowercase_letter = guess_to_check[i].text.lower()
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
                    if indicator.text == lowercase_letter.upper():
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
    current_guess = []
    current_guess_string = ""
    current_letter_bg_x = 110

    if guesses_count == 6 and game_result == "":
        game_result = "L"

def play_again():
    # Puts the play again text on the screen.
    pygame.draw.rect(SCREEN, "white", (10, 600, 1000, 600))
    play_again_font = pygame.font.Font("FreeSansBold.otf", 40)
    play_again_text = play_again_font.render("Press ENTER to Play Again!", True, "black")
    play_again_rect = play_again_text.get_rect(center=(WIDTH/2, 700))
    word_was_text = play_again_font.render(f"The word was {CORRECT_WORD}!", True, "black")
    word_was_rect = word_was_text.get_rect(center=(WIDTH/2, 650))
    SCREEN.blit(word_was_text, word_was_rect)
    SCREEN.blit(play_again_text, play_again_rect)
    pygame.display.update()

def reset():
    # Resets all global variables to their default states.
    global guesses_count, CORRECT_WORD, guesses, current_guess, current_guess_string, game_result
    SCREEN.fill("white")
    SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
    guesses_count = 0
    CORRECT_WORD = random.choice(WORDS)
    guesses = [[]] * 6
    current_guess = []
    current_guess_string = ""
    game_result = ""
    pygame.display.update()
    for indicator in indicators:
        indicator.bg_color = OUTLINE
        indicator.draw()


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
    for guess in guesses:
        for letter in guess:
            letter.draw()

def delete_letter():
    # Deletes the last letter from the guess.
    global current_guess_string, current_letter_bg_x
    guesses[guesses_count][-1].delete()
    guesses[guesses_count].pop()
    current_guess_string = current_guess_string[:-1]
    current_guess.pop()
    current_letter_bg_x -= LETTER_X_SPACING

indicator_enter = Indicator(10,650,"ENTER",83,55)
indicator_delete = Indicator(518,650,"DEL",83,55)
indicator_enter.draw()
indicator_delete.draw()
indicators.append(indicator_enter)
indicators.append(indicator_delete)

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
                    if len(current_guess_string) == 5 and current_guess_string.lower() in WORDS:
                        check_guess(current_guess)
            elif event.key == pygame.K_BACKSPACE:
                if len(current_guess_string) > 0:
                    delete_letter()
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
                    if len(current_guess_string) == 5 and current_guess_string.lower() in WORDS:
                        check_guess(current_guess)
                else:
                    if len(current_guess_string) < 5:
                        create_new_letter(text)
