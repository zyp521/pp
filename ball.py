import pygame
import sys
from pygame import *
import random
import math
pygame.init()
pygame.mixer.init()


size = width,height =1024,681
clock = pygame.time.Clock()
#加载背景音乐
pygame.mixer.music.load(r'../audio/茶烨酱 - 起风了mix (原唱_大神慧).mp3')
pygame.mixer.music.set_volume(0.5)
sound = pygame.mixer.Sound(r'../audio/yinxiao.wav')

screen = pygame.display.set_mode(size)
pygame.display.set_caption('ball')
bg = pygame.image.load('./image/p1.png').convert_alpha()


class Ball(pygame.sprite.Sprite):
    flag=0
    def __init__(self,image,position,speed,bg_size):
         pygame.sprite.Sprite.__init__(self)
         self.image = pygame.image.load(image).convert_alpha()
         self.rect = self.image.get_rect()
         self.rect.left,self.rect.top = position
         #self.rect.center = position
         self.speed = speed
         self.bg_width,self.bg_height = bg_size[0],bg_size[1]
         
    def update(self):
        self.rect =self.rect.move(self.speed)
        #self.rect.centerx += self.speed[0]
        #self.rect.centery += self.speed[1]
        if self.rect.right <= 0:
            self.rect.left = self.bg_width
    
        if self.rect.left > self.bg_width:
            self.rect.right =0
        
        if self.rect.bottom <= 0:
            self.rect.top = self.bg_height #上 if 的条件结果刚好改变 下if的条件会造成不可想象的错误！！！！！！！
            
        if self.rect.top > self.bg_height:
            self.rect.bottom = 0
            
    def change_color(self):
        sound.stop()
        if self.flag==0:
            self.image = pygame.image.load(r'./image/paopao.png').convert_alpha()
            self.flag =1
        elif self.flag==1:
            self.image = pygame.image.load(r'./image/paopao_blue.png').convert_alpha()
            self.flag =0
        sound.play()

def check(item,balls):
     is_collision =False
     for i in balls:
         distance = (i.rect.width + item.rect.width)/2
         dis = math.sqrt((math.pow(i.rect.centerx-item.rect.centerx,2)+\
                          math.pow(i.rect.centery-item.rect.centery,2)))
         if dis <= distance:
             #item.speed[0]=-item.speed[0]
             #item.speed[1]=-item.speed[1]
             is_collision = True
             return is_collision 
             
color=[(0,0,0),(255,255,255),(255,0,0),(0,255,0),(0,0,255)]
Ball_list=[]
image ='./image/paopao.png'
for i in range(5):
    position =(random.randint(0,width-100),random.randint(0,height-100))
    speed =[random.randint(-10,10),random.randint(-10,10)]
    ball = Ball(image,position,speed,size)
    while check(ball,Ball_list):
        position =(random.randint(0,width-100),random.randint(0,height-100))
        ball = Ball(image,position,speed,size)
    Ball_list.append(ball)
    
sprites = pygame.sprite.Group()#创建精灵组
sprites.add(Ball_list)              
 
runing = True
pygame.mixer.music.play(-1)
while runing:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.mixer.music.stop()
            sys.exit()
    screen.blit(bg,(0,0))
    for j in Ball_list:
               screen.blit(j.image,j.rect)
               j.update()
    
    #sprites.draw(screen)
    #sprites.update()
    
    for i  in range(len(Ball_list)):
        temp = Ball_list.pop(i)
        if check(temp,Ball_list):
            temp.speed[0]=-temp.speed[0]
            temp.speed[1]=-temp.speed[1]
            temp.change_color()
        Ball_list.insert(i,temp)
    
        
    pygame.display.flip()
    clock.tick(30)
    
