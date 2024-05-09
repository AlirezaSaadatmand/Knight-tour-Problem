import pygame
from sys import exit
import pyautogui

size = pyautogui.size()
WIDTH , HEIGHT = size
WIDTH , HEIGHT = (WIDTH*9//10) , (HEIGHT*9//10)

UNIT = 80

blocks = []

count_block = 8

class Block:
    def __init__(self , x , y , id , color ):
        self.x = x
        self.y = y
        self.checked = False

        self.id = id
        self.color = color
        if self.color == "white":
            self.text_color = "black"
        else:
            self.text_color = "white"

    def draw(self):
        sur = pygame.Surface( (UNIT , UNIT) )
        sur.fill(self.color)
        sur_rect = sur.get_rect(topleft = (self.x , self.y))
        screen.blit(sur , sur_rect)

        text = pygame.font.Font(None , 30)
        text = text.render(f"{self.id}" , self.text_color , True)
        text_rect = text.get_rect(center = (self.x + (UNIT / 2) , self.y + (UNIT / 2)))
        screen.blit(text , text_rect)


def create_board():

    y = (HEIGHT / 2) - (UNIT * count_block / 2)
    id = 1
    color = "black"
    for _ in range(count_block):
        x = (WIDTH / 2) - (UNIT * count_block / 2)
        for _ in range(count_block):
            blocks.append(Block(x , y , id , color))
            if id % 8 != 0:
                if color == "white":
                    color = "black"
                else:
                    color = "white"
            x += UNIT
            id += 1
        y += UNIT
    
create_board()

def draw():
    screen.fill("#f59563")
    for block in blocks:
        print(block.text_color)
        block.draw()
    
pygame.init()
screen = pygame.display.set_mode( (WIDTH , HEIGHT) )
screen.fill("#f59563")
pygame.display.set_caption("KNIGHT PROBLEM")
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    draw()
    pygame.display.update()
    clock.tick(10)