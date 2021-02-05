import pygame_menu


def create_menu(start_the_game, screen):
    menu = pygame_menu.Menu(300, 400, 'Welcome',
                            theme=pygame_menu.themes.THEME_BLUE)

    menu.add_text_input('Name :', default='John Doe')
    menu.add_button('Play', start_the_game)
    menu.add_button('Quit', pygame_menu.events.EXIT)

    menu.mainloop(screen)
