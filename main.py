import pygame
import pygame_menu
from game import *



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

def set_difficulty(value, difficulty):
    # Do the job here !
    pass


def start_the_game():
    user_age = nick.get_value()
    diff = diff.get_value()
    print(user_age)  # to print the value of user_age, only for debugging tho, don't use this when you have finished the game, because user is not really supposed to read the console anyways

    # rest of the game code



glob_sets = browse()
x, y = glob_sets['x'], glob_sets['y']
g_modes = [('Standart', 1), ('Advansed', 2)]

pygame.init()
surface = pygame.display.set_mode((x, y))

menu = pygame_menu.Menu('Welcume', x, y,theme=pygame_menu.themes.THEME_BLUE)
nick = menu.add.text_input('Никнейм :', default=glob_sets['last_nick'], maxchar=30)
diff = menu.add.selector('Режим игры:', g_modes, )


menu.add.button('Играть', start_the_game)
menu.add.button('Выход', pygame_menu.events.EXIT)
menu.mainloop(surface)
