# 系统函数容易忘记，如果把系统函数封装起来实现我们自己的类，
# 并且加入一些定制化功能，那么调用起来一定会更加方便
import pygame

# 继承自 Sprite 类可以让你使用 Pygame 的Group功能
# 方便管理游戏中的多个对象
class Image(pygame.sprite.Sprite):
    # __init__ 是类的构造函数，当创建 Image 对象时，会自动运行
    # self 代表当前创建的对象本身
    def __init__(self,path):
        # 将传入的路径保存到 self.path 属性中，以便后续使用
        self.path = path

        self.image = pygame.image.load(self.path)

    def draw(self,ds):
        # ds.blit() 函数把 self.image 绘制到 ds 上
        # ds为self.image.get_rect() 获取到的图片矩形区域
        ds.blit(self.image,self.image.get_rect())