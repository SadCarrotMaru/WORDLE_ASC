import pygame       # asta il stiti
pygame.init()       # initializezi aplicatia
# Constants
WIDTH, HEIGHT = 500, 500       # dimensiunile aplicatiei 

ICON = pygame.image.load("Icon.png")       # iconita aplicatiei ( tot in fisier e)

pygame.display.set_caption("Wordle - Sad Carrot Team")  # cum se numeste aplicatia
pygame.display.set_icon(ICON)                # seteaza iconita

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)
 
 
class Button:
    """Create a button, then blit the surface in the while loop"""
 
    def __init__(self, text,  pos, font, bg="black", feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback
        self.change_text(text, bg)
 
    def change_text(self, text, bg="black"):
        """Change the text whe you click"""
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
 
    def show(self):
        screen.blit(self.surface, (self.x, self.y))
 
    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.feedback, bg="red")
 
 
def mainloop():
    """ The infinite loop where things happen """
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            button2.click(event)
            button1.click(event)
        button2.show()
        button1.show()
        clock.tick(30)
        pygame.display.update()
 
button2 = Button(
    "Click here aa",
    (200, 300),
    font=30,
    bg="navy",
    feedback="You clicked me")

button1 = Button(
    "Click here",
    (200, 100),
    font=30,
    bg="navy",
    feedback="You clicked me")
 
mainloop()