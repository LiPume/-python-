# 主窗口
# 导入主要工具pygame库
import pygame
# 导入所有常量，如QUIT
from pygame.locals import *
# 导入sys库，用于与Python解释器交互
import sys
from const import *
from game import *
# 初始化pygame所有模块
pygame.init()

# 创建一个画布：一个指定尺寸的窗口，并返回一个 Surface 对象
DS = pygame.display.set_mode((1280 , 600))
game = Game(DS)


# 游戏主循环
while True:
    # 遍历事件队列，获取所有发生的事件（比如鼠标点击、键盘输入、关闭窗口等）
    for event in pygame.event.get():
        # 检测事件类型
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game.mouseClickHandler(event.button)

    # 用白色 (255,255,255) 填充整个窗口
    DS.fill((255,255,255))

    game.update()
    game.draw()

    pygame.display.update()

