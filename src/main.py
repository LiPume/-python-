# 主窗口
import pygame
from pygame.locals import *
import sys
pygame.init()

DS = pygame.display.set_mode((1280 , 600))  # 创建窗口

image = pygame.image.load('../pic/other/back.png')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DS.fill((255,255,255))
    DS.blit(image,image.get_rect())
    pygame.display.update()

