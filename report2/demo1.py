import pygame,sys,math

pygame.init()

FPS=10
fpsClock=pygame.time.Clock()

DISPLAYS=pygame.display.set_mode((1440,900))
pygame.display.set_caption("MY ANM")

BLUE=(255,255,255)
GRAY=(192,192,192)
canon=pygame.image.load('canon.png')
bgm=pygame.image.load('bgm.jpg')
G=10
angle=math.pi/4
canonv0=110
canonvx=int(canonv0*math.cos(angle))
canonvy=int(canonv0*math.sin(angle))
canonx=10
canony=868
    
direction='up'

while True:
    DISPLAYS.fill(BLUE)
    if direction=='up':
        canonx=canonx+canonvx
        canony=canony-canonvy
        canonvx=canonvx
        canonvy=canonvy-10
          
    DISPLAYS.blit(bgm,(0,0))
    DISPLAYS.blit(canon,(canonx,canony))
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    fpsClock.tick(FPS)
        
    
        