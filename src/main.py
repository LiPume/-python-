# 主窗口
# 导入主要工具pygame库
import pygame
# 导入所有常量，如QUIT
from pygame.locals import *
# 导入sys库，用于与Python解释器交互
import sys
from const import *
# 初始化pygame所有模块
pygame.init()

# 创建一个画布：一个指定尺寸的窗口，并返回一个 Surface 对象
DS = pygame.display.set_mode((1280 , 600))

# 导入自定义的image模块
import image
import zombiebase
import peabullet
# 使用自定义的image类导入背景图片
# image = pygame.image.load('../pic/other/back.png')

img = image.Image(PATH_BACK,0,(0,0),GAME_SIZE,0)
zom = zombiebase.ZombieBase(0,(1000,200))
pb = peabullet.PeaBullet(0,(0,200))
# 游戏主循环
while True:
    # 遍历事件队列，获取所有发生的事件（比如鼠标点击、键盘输入、关闭窗口等）
    for event in pygame.event.get():
        # 检测事件类型
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # 用白色 (255,255,255) 填充整个窗口
    DS.fill((255,255,255))
    # DS.blit(image,image.get_rect())

    # 调用自定义 Image 类的 draw 方法，把图片绘制到 DS 这个窗口上
    img.draw(DS)

    zom.update()
    zom.draw(DS)
    # 更新整个窗口的显示内容，把上面绘制的图片显示出来
    pb.update()
    pb.draw(DS)
    pygame.display.update()

