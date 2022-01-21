import pygame
import pygame_menu

f = open('settings.txt', 'r')
ss = {}
for line in f:
    item = line.strip('\n').replace(' ', '').split('=')

    try:
        ss[item[0]] = int(item[1])
    finally:
        ss[item[0]] = item[1]

pygame.init()
surface = pygame.display.set_mode((800, 600))

def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    user_age = age_input.get_value()
    print(user_age)  # to print the value of user_age, only for debugging tho, don't use this when you have finished the game, because user is not really supposed to read the console anyways
    # rest of the game code



def aa(*g, **gg):
    print(g, gg)

menu = pygame_menu.Menu('Welcome', 800, 600,
                       theme=pygame_menu.themes.THEME_BLUE)
user_input=''
g_modes = [('Standart', 1), ('Advansed', 2)]
nick = ''
menu.add.text_input('Никнейм :', default='Nagibator777', onreturn=aa, maxchar=30)
menu.add.selector('Режим игры:', g_modes, onchange=set_difficulty)
age_input = menu.add.text_input('User: ')
menu.add.button('Comencem', start_the_game)


menu.add.button('Играть', start_the_game)
menu.add.button('Выход', pygame_menu.events.EXIT)
menu.mainloop(surface)
menu.disable()
print(user_input)