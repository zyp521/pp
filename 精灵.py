import pygame
import sys

size=width,height=400,600
color_white=(255,255,255)
color_black = (0,0,0)
color_red = (255,0,0)
color_blue = (0,0,255)
fps=60
clock=pygame.time.Clock()#实例化一个时钟对象
pygame.init()

screen=pygame.display.set_mode(size)#初始化窗口或屏幕以进行显示
pygame.display.set_caption('demo game')#设置当前窗口标题


all_sprites = pygame.sprite.Group()#精灵组类


#创建红精灵
class Player1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,30))#实例化一个面对象
        self.image.fill(color_red)
        self.rect = self.image.get_rect()#得到表面的矩形区域对象
        #slef.rect.center=(0,0)默认位置
        self.rect.x = width/2
        self.rect.y = height - 300
    def update(self):
        self.rect.x +=2
        self.rect.y -=1
        if self.rect.x > width:
            self.rect.x = 0-29
        if self.rect.bottom <0:
            self.rect.y = height 
            

#创建蓝精灵
class Player2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))#实例化一个面对象
        self.image.fill(color_blue)
        self.rect = self.image.get_rect()#得到表面的矩形区域对象
        self.rect.x  = width / 2
        self.rect.y = height - 200
    def update(self):
        self.rect.x -=2
        self.rect.y +=1
        if self.rect.right < 0:
            self.rect.x = width-1
        if self.rect.top > height:
            self.rect.y = 0-50
            
player1 = Player1()
player2 = Player2()

all_sprites.add(player1,player2)

runing=True
while runing:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
            
    screen.fill(color_white)      
    all_sprites.draw(screen)#所有精灵写入画面(窗口)      
    all_sprites.update()#对其内所有精灵调用自身update()
    
    
    pygame.display.flip()#更新整个显示的内容
    
    clock.tick(fps)  # 通过时钟对象指定循环频率
        
            
                                 


