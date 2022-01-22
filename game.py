def browse_glob_data(txt_name='settings.txt'):
    '''функция для получения данных из текстовика в форме словаря
    :return dict'''
    ss = {}
    for line in open(txt_name, 'r'):
        item = line.strip('\n').replace(' ', '').split('=')
        try:
            ss[item[0]] = int(item[1])
        except ValueError:
            ss[item[0]] = item[1]
    return ss

def save_glob_data(thing, txt_name='settings.txt'):
    '''фенкция для сохранения словаря/котрежа/списка в текстовик
    :arg thing - что сохранить'''
    for i in thing.items:
        print(i)

def start_menu(nick, g_modes):
    import pygame
    import pygame_menu

    def set_difficulty(value, difficulty):
        global diff
        diff = 1
        diff = difficulty

    def start_the_game():
        user_age = text_input.get_value()
        print(user_age, diff)

    diff = 1
    pygame.init()
    surface = pygame.display.set_mode((800, 450))

    menu = pygame_menu.Menu('Welcome', 800, 450, theme=pygame_menu.themes.THEME_BLUE)
    text_input = menu.add.text_input('Никнейм :', default=nick, maxchar=30)
    menu.add.selector('Режим игры:', g_modes, onchange=set_difficulty)
    menu.add.button('Играть', start_the_game)
    menu.add.button('Выход', pygame_menu.events.EXIT)
    menu.mainloop(surface)





