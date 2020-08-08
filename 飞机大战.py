import pygame
import sys
import time
import random

#初始化
pygame.init()
pygame.font.init()
size=width,height = 480,652
background = pygame.image.load(r'./image/star.jpg')#从文件加载新图片
clock = pygame.time.Clock()
font_name = pygame.font.match_font('simhei')



#控制重复按键响应时间（第一次响应时间，两次响应时间间隔）
pygame.key.set_repeat(50,50)



screen =pygame.display.set_mode(size)
pygame.display.set_caption('飞机大战')
pygame.display.set_icon(pygame.image.load(r'./image/icon.jpg'))#设置窗口图标


#游戏界面文字添加
def draw_text(surf,text,size,x,y):
    font = pygame.font.Font(font_name,size)
    text_surface = font.render(text,True,(255,255,255))#产生包含文字的surface对象
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface,text_rect)


    
#检测碰撞函数
def impact(plan,biu_list):
    for biu in biu_list:
        for lis in plan.blast:
            start_x,end_x = plan.x +lis['x'][0],plan.x+lis['x'][1]
            start_y,end_y = plan.y +lis['y'][0],plan.y+lis['y'][1]
            if (start_x < biu.x < end_x) and (start_y < biu.y < end_y):
                plan.bomb()
                biu_list.remove(biu)

        
#kongzhi飞机移动
def kongzhi(hero_tmp):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:#有键盘按下
            if event.key == pygame.K_LEFT:
                hero_tmp.move_left()
            if event.key == pygame.K_RIGHT:
                hero_tmp.move_right()
            if event.key == pygame.K_SPACE:
                hero_tmp.fire()
            if event.key == pygame.K_UP:
                hero_tmp.move_top()
            if event.key == pygame.K_DOWN:
                hero_tmp.move_bottom()
            
    
            
              

#玩家子弹类
class Biu:
    x = 0
    y = 0
    biu_img = pygame.image.load(r'./image/zidan.png')
    def __init__(self,surface,plan_x,plan_y):
        self.surface =surface
        self.x = plan_x + 50
        self.y = plan_y 
    def biu_display(self):
        self.surface.blit(self.biu_img,(self.x,self.y))
    def move_up(self):
        self.y -=10



#敌机子弹类
class EnemyBiu:
    x = 0
    y = 0
    biu_img = pygame.image.load(r'./image/zidan.png')
    def __init__(self,surface,plan_x,plan_y):
        self.surface =surface 
        self.x = plan_x + 50
        self.y = plan_y + 100
    def biu_display(self):
        self.surface.blit(self.biu_img,(self.x,self.y))
    def move_up(self):
        self.y +=3

        

#创建玩家飞机类
class HeroPlan():
    image = ['./image/feiji1.png','./image/feiji2.png','./image/feiji3.png',\
             './image/feiji4.png']
    bomb_img = ['./image/feiji_baozha1.png','./image/feiji_baozha2.png',\
                './image/feiji_baozha3.png','./image/feiji_baozha4.png']
    
    x = 190#初始位置
    y = 550

    biu_list = []#子弹列表
    
    img_index = 0
    
    is_bomb = False

    #碰撞有效区域
    blast = [{'x':(27,81),'y':(27,80)},{'x':(0,0),'y':(0,0)}]
    def __init__(self,surface):
        self.surface = surface
    def hero_display(self):
        #检查玩家飞机是否爆炸并绘制图片
        if self.is_bomb == False:
            self.surface.blit(pygame.image.load(self.image\
                                [self.img_index]),(self.x,self.y))
        else:
            time.sleep(0.2)
            self.surface.blit(pygame.image.load(self.bomb_img[self.img_index\
                                            ]),(self.x,self.y))
            time.sleep(0.5)
            self.img_index += 1
            if self.img_index == len(self.bomb_img):
                              sys.exit('游戏结束')
            self.is_bomb = False
        
        for biu in self.biu_list:
                              biu.biu_display()#绘制子弹
                              biu.move_up()#移动子弹
                              #超出窗口则删除子弹
                              self.biu_list.remove(biu) if biu.y <0 else ''
    def fire(self):
        #存一颗子弹进入子弹列表
        self.biu_list.append(Biu(self.surface,self.x,self.y))
    def move_right(self):
        #限制玩家飞机的移动范围
        if self.x < 380:
            self.x += 10
    def move_left(self):
         #限制玩家飞机的移动范围
        if self.x > 0:
            self.x -=10 
    def move_top(self):
        if self.y >100:
            self.y -=10
    def move_bottom(self):
        if self.y < 550:
            self.y +=10
    def bomb(self):
        self.is_bomb = True


#创建敌机类
class EnemyPlan():
    image = ['./image/feiji1.png','./image/feiji2.png','./image/feiji3.png',\
             './image/feiji4.png']
    bomb_img = ['./image/feiji_baozha1.png','./image/feiji_baozha2.png',\
                './image/feiji_baozha3.png','./image/feiji_baozha4.png']
    
    x = 190#初始位置
    y = -5  
    direction = 'right'

    biu_list = []#子弹列表
    img_index = 0
    is_bomb = False

    #碰撞有效区域
    blast = [{'x':(27,81),'y':(27,80)},{'x':(0,0),'y':(0,0)}]
    
    def __init__(self,surface):
        self.surface = surface
    def display(self):
        
        #敌机飞机是否爆炸并绘制图片
        if self.is_bomb == False:
            self.surface.blit(pygame.transform.flip(pygame.image.load\
                                        (self.image[self.img_index]),False,True),(self.x,self.y))
        else:
            time.sleep(0.5)
            self.surface.blit(pygame.image.load(self.bomb_img[self.img_index\
                                            ]),(self.x,self.y))
            time.sleep(0.5)
            self.img_index += 1
            if self.img_index == len(self.bomb_img):
                              sys.exit('游戏结束')
            self.is_bomb = False
        
        for biu in self.biu_list:
                              biu.biu_display()#绘制子弹
                              biu.move_up()#移动子弹
                              #超出窗口则删除子弹
                              self.biu_list.remove(biu) if biu.y > height else ''
    def fire(self):
        #存一颗子弹进入子弹列表
        self.biu_list.append(EnemyBiu(self.surface,self.x,self.y))
    def move(self):
        #判断敌机移动方向
        if self.direction == 'right':
            if self.x > 380:
                self.direction = 'left'
            self.x += 1
        if self.direction == 'left':
            if self.x <= 0:
                self.direction = 'right'
            self.x -= 1
        num = random.randint(1,100)
        if num == 50 or num ==100:
            self.fire()
    def bomb(self):
        self.is_bomb = True
    

        

#游戏启动界面
def start_screen():
    screen.blit(background,(0,0))
    draw_text(screen,'Start the game',64,480/2,652/4)
    draw_text(screen,'Press the left and right arrow to move, press the space bar to shoot',22,480/2,652/2)
    draw_text(screen,'Press any key to start the game',18,480/2,652*3/4)
    pygame.display.flip()
    
    waiting=True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYUP:
                waiting = False
            
       
hero = HeroPlan(screen)
enemyplan = EnemyPlan(screen)

start_screen()
while True:
    screen.blit(background,(0,0))#加入背景图片
    
    hero.hero_display()#绘制玩家飞机
    kongzhi(hero)#控制玩家飞机
    
    
    enemyplan.display()#绘制敌机
    enemyplan.move()#控制敌机移动
    
    #检测碰撞玩家飞机与敌机子弹
    impact(hero,enemyplan.biu_list)
     #检测碰撞玩家飞机与敌机子弹
    impact(enemyplan,hero.biu_list)
    
    pygame.display.update()#更新部分游戏窗口（无参数==flip())
    clock.tick(60)
