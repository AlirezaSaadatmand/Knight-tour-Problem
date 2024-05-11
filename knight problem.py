import pygame
from sys import exit
import pyautogui

size = pyautogui.size()
WIDTH , HEIGHT = size
WIDTH , HEIGHT = (WIDTH*9//10) , (HEIGHT*9//10)

UNIT = 50

blocks = []

count_block = 12


knight_position = 1

class Block:
    def __init__(self , xpos , ypos , x , y , id , color):
        
        self.xpos = xpos
        self.ypos = ypos
        
        self.x = x
        self.y = y
        self.checked = False
        
        self.neighbors = []

        self.id = id
        self.color = color
        if self.color == "white":
            self.text_color = "black"
        else:
            self.text_color = "white"
    
    def get_neighbor(self):
        self.neighbors = []
        x = self.xpos
        y = self.ypos
        topLeft = [x-1 , y -2]
        topRight = [x+1 , y -2]
        buttomLeft = [x-1 , y +2]
        buttomRight = [x+1 , y +2]
        leftTop = [x-2 , y -1]
        leftButtom = [x-2 , y +1]
        rightTop = [x+2 , y -1]
        rightButtom = [x+2 , y +1]
        
        for block in blocks:
            if [block.xpos , block.ypos] in [topLeft , topRight , buttomLeft , buttomRight , leftTop , leftButtom , rightTop , rightButtom] and block.checked == False:
                self.neighbors.append(block)
        
    def move(self):
        lst = []
        for n in self.neighbors:
            n.get_neighbor()
            if len(n.neighbors) > 0:
                lst.append(len(n.neighbors))
        if lst:
            r = lst.index(min(lst))
            return self.neighbors[r].id
        else:
            return False
    def draw(self):
        if self.checked :
            self.color = "yellow"
        sur = pygame.Surface( (UNIT , UNIT) )
        sur.fill(self.color)
        sur_rect = sur.get_rect(topleft = (self.x , self.y))
        screen.blit(sur , sur_rect)
        pygame.draw.rect(screen , "black", sur_rect,  1, 0)
        



def create_board():

    y = (HEIGHT / 2) - (UNIT * count_block / 2)
    id = 1
    color = "black"
    for i in range(count_block):
        x = (WIDTH / 2) - (UNIT * count_block / 2)
        for j in range(count_block):
            blocks.append(Block( j , i , x , y , id , color))
            if id % count_block != 0:
                if color == "white":
                    color = "black"
                else:
                    color = "white"
            x += UNIT
            id += 1
        y += UNIT
    
create_board()

def move(knight_position):

    for block in blocks:
        if block.id == knight_position:
            block.get_neighbor()
            return block.move()          

def draw(screen):
    screen.fill("#f59563")
    for block in blocks:
        block.draw()


pygame.init()
screen = pygame.display.set_mode( (WIDTH , HEIGHT) )
screen.fill("#f59563")
pygame.display.set_caption("KNIGHT PROBLEM")
clock = pygame.time.Clock()

running = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if running:    
        knight_position = move(knight_position)
        if knight_position == False:
            for block in blocks:
                if block.checked == False:
                    knight_position = block.id
                    running = False
        for block in blocks:
            if block.id == knight_position:
                block.checked = True
                
        draw(screen)
    pygame.display.update()
    clock.tick(5)