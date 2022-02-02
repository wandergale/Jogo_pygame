from jogo_3 import *
import pygame, sys, time
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('menu')

font = pygame.font.SysFont(None, 20)

BACK = (255, 64, 64)
BACKGROUND = pygame.image.load("C:/Users/wande/Documents/PROJECTS/Python/Jogo_pygame/Jogo_starwars/imagens/menu_han_solo.jpg")

def desenhar_txt(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_menu():
    click = False
    screen.blit(BACKGROUND,(0,0))
    pygame.mixer.music.load("C:/Users/wande/Documents/PROJECTS/Python/Jogo_pygame/Jogo_starwars/Musica/star_wars.mp3")
    pygame.mixer.music.play()
    while True:

        screen.fill((0,0,0))
        screen.blit(BACKGROUND,(0,0))
        desenhar_txt('main menu', font, (255,255,255), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        # button_1 = draw_text('Play', font, (255,0,0), screen, 20, 40)
        # button_2 = draw_text('Exit', font, (255,0,0),screen, 20, 60)
        button_1 = pygame.Rect(50, 100, 20, 20)
        desenhar_txt('Play', font, (255,0,0), screen, 20, 100)
        button_2 = pygame.Rect(50, 200, 20, 20)
        desenhar_txt('Exit', font, (255,0,0), screen, 20, 200)
        if button_1.collidepoint((mx, my)):
            if click:
                game()

        if button_2.collidepoint((mx, my)):
            if click:
                print('Finalizando',end='')
                for i in range(3):
                    print(1*'.',end='', flush=True)
                    time.sleep(0.5)
                print()
                try:
                    print()
                    for jogador, score in enumerate(lista_score):
                        print(f'Jogador {jogador+1}, score: {score}')
                    print()
                    print(f'MAIOR SCORE: {max(lista_score)}, jogador: {lista_score.index(max(lista_score))+1}')
                except:
                    pass
                pygame.quit()
                sys.exit()
    
        pygame.draw.rect(screen, (255,0,0), button_1)
        pygame.draw.rect(screen, (255,0,0), button_2)
        
        click = False
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


        pygame.display.update()

main_menu()