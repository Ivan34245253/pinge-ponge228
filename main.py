import pygame
from random import randint
pygame.init()
clock = pygame.time.Clock()
mw = pygame.display.set_mode((500, 500)) 
back = (200,100,255)
mw.fill(back)

RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 51)

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x,y,width,height)
        self.fill_color = back
        self.xmove = 2
        self.ymove = 2
        if color:
            self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw,self.fill_color,self.rect)

    def move_x(self):
        self.rect.x += self.xmove
    def move_y(self):
        self.rect.y += self.ymove

class Lable(Area):  
    def set_text(self, text, fsize=12, text_color=(0,0,0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))   

class Picture(Area):
    def __init__(self,filename,x=0,y=0,width=10,height=10):
        Area.__init__(self,x=x,y=y,width=width,height=height,color=None)
        self.image = pygame.image.load(filename)
    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))  
    def colliderect(self,rect):
        return self.rect.colliderect(rect)


ball = Picture('ball.png',160,200,50,50)
platform = Picture('platform.png',10,10,30,150)
platform2 = Picture('platform2.png',460,350,30,150)
my_win = Lable(150, 200, 50, 50, back)
my_lose = Lable(150, 200, 50, 50, back)

game1 = True
game_over = False 
move_down = False
move_up = False
move_down2 = False
move_up2 = False

start_x = 5
start_y = 5
count = 9

while not game_over:
    ball.fill()
    platform.fill()
    platform2.fill()
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if game1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    move_up = True
                if event.key == pygame.K_s:
                    move_down = True

                if event.key == pygame.K_UP:
                    move_up2 = True
                if event.key == pygame.K_DOWN:
                    move_down2 = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    move_up = False
                if event.key == pygame.K_s:
                    move_down = False

                if event.key == pygame.K_UP:
                    move_up2 = False
                if event.key == pygame.K_DOWN:
                    move_down2 = False
 
    if move_up:
        platform.rect.y -= 5
      
    if move_down:
        platform.rect.y += 5

    if move_up2:
        platform2.rect.y -= 5
      
    if move_down2:
        platform2.rect.y += 5
    
    ball.move_x()
    ball.move_y()

    if ball.rect.x > 490:
        my_lose.set_text('Негры победили(',20,(220,0,0))
        my_lose.draw()
        game1 = False
    elif ball.rect.x < 10:
        my_win.set_text('Победили белые!',20,(0,220,0))
        my_win.draw()
        game1 = False
        

    if ball.rect.y < 0 or ball.rect.y > 450:
        ball.ymove *=- 1
    if  ball.rect.colliderect(platform.rect) or ball.rect.colliderect(platform2.rect):
        ball.xmove *=- 1

    platform.draw() 
    platform2.draw()      
    ball.draw()

    pygame.display.update()
    clock.tick(80)

