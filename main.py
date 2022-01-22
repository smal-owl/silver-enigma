import pygame
import pygame_menu
from game import *

'''----------------globals---------------'''
global xy
glob_data = browse_glob_data()
xy = (glob_data['x'], glob_data['y'])
nick = glob_data['last_nick']
g_modes = [('Standart', 1), ('Advansed', 2)]

'''class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, 'white',
                                 (x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                                  self.cell_size), True)




try:
    pygame.init()
    pygame.display.set_caption('finaly')
    size = width, height = 16*50, 9*50
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    screen.fill((255, 0, 255))
    running = True

    while running:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT or event.type == 32784:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        screen.fill((0, 0, 0))
        pygame.display.flip()
        clock.tick(60)
except Exception as e:
    print(e)

pygame.quit()
'''

start_menu(nick, g_modes)





