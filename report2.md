# Report 2 : A Cannon Shell
### Author: Cathaya Liu ,   [*WHU*](http://physics.whu.edu.cn/)

***

## 一、Sorry
因为电脑出了问题去送修了，在网吧简单写了个沿着抛物线运动的pygame小程序。完整版本的Report将在下周六前提交，请见谅。

## 二、程序的Python实现
```
#导入各模组
import pygame,sys,math

pygame.init()

#设定帧率
FPS=10
fpsClock=pygame.time.Clock()

#绘制显示窗口
DISPLAYS=pygame.display.set_mode((1440,900))
pygame.display.set_caption("MY ANM")

#定义各个变量
WHITE=(255,255,255)
canon=pygame.image.load('canon.png')
bgm=pygame.image.load('bgm.jpg')
G=10 #加速度
angle=math.pi/4 #发射角
canonv0=110 #发射速度
canonvx=int(canonv0*math.cos(angle)) #x方向速度
canonvy=int(canonv0*math.sin(angle)) #y方向速度
canonx=10 #初始位置
canony=868 #初始位置
direction='up'

#游戏主循环
while True:
    DISPLAYS.fill(WHITE)
    if direction=='up':
        canonx=canonx+canonvx
        canony=canony-canonvy
        canonvx=canonvx
        canonvy=canonvy-10

#绘制动画和背景图
    DISPLAYS.blit(bgm,(0,0))
    DISPLAYS.blit(canon,(canonx,canony))
    
#退出程序
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
     
#输出动画至窗口     
    pygame.display.update()
    fpsClock.tick(FPS)
```
## 三、一些说明
运行时必须将canon.png和bgm.jpg放在与python程序相同的文件夹下，否则会报错。
所有图片资源来自淘宝购买素材库，仅用作学习，侵删。
