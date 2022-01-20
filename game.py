import math
import pygame


x = 16*50
y = 9*50

def browse(txt_name='settings.txt'):
    ss = {}
    for line in open(txt_name, 'r'):
        item = line.strip('\n').replace(' ', '').split('=')
        try:
            ss[item[0]] = int(item[1])
        finally:
            ss[item[0]] = item[1]
    return ss


class Ball():
    def __init__(self, screen, board, x , y, angl, r=10, spd = 2):
        self.board = board
        self.x = x
        self.y = y
        self.r = r
        self.speed = spd
        self.x_speed = math.cos(angl) * self.speed
        self.y_speed = math.sin(angl) * self.speed



    def update(self):
        ##simple drawing


    def collide(self):
        ##изменение угла, столкновение об


    def find_near(self):
        ##нахождение ближайших объектов для коллизии
        pass


